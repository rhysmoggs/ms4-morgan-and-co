from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from products.models import Product
# from profiles.models import UserProfile
from django.contrib.auth.models import User


@login_required
def add_review(request, product_id):
    """ Allows a user to add a review """

    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(User, username=request.user)

    if request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.review_author = user
            review.save()
            messages.success(request, 'Thank You! Your review \
                has been added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Oops, something went wrong! \
                Please try adding your review again.')

    context = {
        'form': form,
    }

    return render(request, context)


@login_required
def edit_review(request, review_id):
    """ Edit a product review """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('home'))

    review = get_object_or_404(Review, id=review_id)
    product = review.product
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update your review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {product.name}')

    template = 'reviews/edit_reviews.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a product review """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('home'))
    review = get_object_or_404(Review, id=review_id)
    product = review.product

    review.delete()

    messages.success(request, f'{product.name} review removed!')

    return redirect(
        # reverse('product_detail', kwargs={"product_id": product.id}))
        reverse('product_detail', args=[product.id]))
