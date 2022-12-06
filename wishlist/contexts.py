from django.shortcuts import get_object_or_404

from wishlist.models import Wishlist
from profiles.models import UserProfile


def wishlist_contents(request):

    """ A view to return the wishlist page """
    wishlist = None

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        print(user)
        try:
            get_user_wishlist = Wishlist.objects.get(user=user)
            print(get_user_wishlist)
            wishlist = get_user_wishlist.products.all()
            print(wishlist)
        except Wishlist.DoesNotExist:
            pass

    context = {
        'wishlist': wishlist,
    }

    return context
