from django.shortcuts import render


def about(request):
    """ A view to return the About Us page """

    return render(request, 'about/about.html')
