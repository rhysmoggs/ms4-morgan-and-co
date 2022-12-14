from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import Product, Category, Room, Special
from .forms import ProductForm

from django.contrib.auth.models import User
from profiles.models import UserProfile
from wishlist.models import Wishlist
from reviews.models import Review
from reviews.forms import ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    rooms = None
    specials = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'room':
                sortkey = 'room__name'
            if sortkey == 'special':
                sortkey = 'special__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'room' in request.GET:
            rooms = request.GET['room'].split(',')
            products = products.filter(room__name__in=rooms)
            rooms = Room.objects.filter(name__in=rooms)

        if 'special' in request.GET:
            specials = request.GET['special'].split(',')
            products = products.filter(special__name__in=specials)
            specials = Special.objects.filter(name__in=specials)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_rooms': rooms,
        'current_specials': specials,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    reviews_by_user = None
    check_wishlist = None

    if request.user.is_authenticated:
        reviews_by_user = Review.objects.filter(
            product=product,
            review_author=get_object_or_404(User, username=request.user)
        )

        user = get_object_or_404(UserProfile, user=request.user)
        try:
            get_user_wishlist = Wishlist.objects.get(user=user)
            check_wishlist = get_user_wishlist.products.all()
        except Wishlist.DoesNotExist:
            pass
        check_wishlist = Wishlist.objects.filter(user=user, products=product)

    form = ReviewForm()

    average_rating = reviews.aggregate(
        Avg('review_rating'))['review_rating__avg']

    product.save()

    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'average_rating': average_rating,
        'reviews_by_user': reviews_by_user,
        'check_wishlist': check_wishlist
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form \
                    is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is \
                    valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
