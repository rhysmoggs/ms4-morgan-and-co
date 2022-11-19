from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Wishlist
from profiles.models import UserProfile


@login_required
def get_wishlist(request):
    """ A view to return the wishlist page """

    user = get_object_or_404(UserProfile, user=request.user)
    print(user)

    wishlist = None
    print(wishlist)

    # try to get the user wishlist, if it exists
    try:
        get_user_wishlist = Wishlist.objects.get(user=user)
        print(get_user_wishlist)
        wishlist = get_user_wishlist.products.all()
        print(wishlist)
    except Wishlist.DoesNotExist:
        pass

    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)
