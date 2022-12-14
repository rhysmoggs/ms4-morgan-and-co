from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from products.models import Product
from profiles.models import UserProfile


@login_required
def get_wishlist(request):
    """ A view to return the wishlist page """

    template = 'wishlist/wishlist.html'

    return render(request, template)


@login_required
def add_to_wishlist(request, product_id):
    """ A view to add a product to user wishlist """

    # get current product
    product = get_object_or_404(Product, pk=product_id)

    # get current user
    user = get_object_or_404(UserProfile, user=request.user)

    # get user wishlist otherwise create wishlist
    wishlist, created = Wishlist.objects.get_or_create(user=user)

    # check if product exists in user wishlist
    check_duplicate = bool(
        Wishlist.objects.filter(user=user, products=product))

    # if product exists in user wishlist, inform user, else, add
    #  to user wishlist
    if check_duplicate:
        messages.info(request, f'{product.name} already in your wishlist.')
    else:
        wishlist.products.add(product)
        messages.success(request, f'{product.name} added to your wishlist.')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def remove_from_wishlist(request, product_id):
    """ Remove product from user wishlist """

    # get current product
    product = get_object_or_404(Product, pk=product_id)

    # get user wishlist
    wishlist = Wishlist.objects.get(user=request.user.userprofile)

    # remove product from the wishlist
    wishlist.products.remove(product)
    messages.success(
        request, f'{product.name} was removed from your wishlist.')

    return redirect(reverse('wishlist'))
