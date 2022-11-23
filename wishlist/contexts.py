from django.shortcuts import get_object_or_404
# from django.contrib.auth.models import AnonymousUser

# from products.models import Product
from wishlist.models import Wishlist
from profiles.models import UserProfile


# LoginRequiredMixin  ???

def wishlist_contents(request):

    """ A view to return the wishlist page """

    # user = request.user if type(request.user) is not AnonymousUser else None
    # print(user)

    # try:
    #     UserProfile.objects.get(user=user)
    # except UserProfile.DoesNotExist:
    #     pass
    wishlist = None

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        print(user)

        # try to get the user wishlist, if it exists
        # try:
        #     wishlist = Wishlist.objects.get(user=user)
        #     print(wishlist)
        #     wishlist.products.all()
        #     print(wishlist.products.all())
        # except Wishlist.DoesNotExist:
        #     pass
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


# def wishlist_contents(request):

#     """ A view to return the wishlist page """

#     user = get_object_or_404(UserProfile, user=request.user)
#     print(user)

#     my_wishlist = None
#     print(my_wishlist)

#     # try to get the user wishlist, if it exists
#     try:
#         get_my_wishlist = Wishlist.objects.get(user=user)
#         print(get_my_wishlist)
#         my_wishlist = get_my_wishlist.products.all()
#         print(my_wishlist)
#     except Wishlist.DoesNotExist:
#         pass

#     context = {
#         'my_wishlist': my_wishlist,
#     }

#     return context
