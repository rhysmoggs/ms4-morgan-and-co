from django.shortcuts import render


def index(request):
    """ A view to return the home page """

    return render(request, 'home.html')


def contact(request):
    """ A view to return the Contact Us page """

    return render(request, 'contact.html')


def about(request):
    """ A view to return the About Us page """

    return render(request, 'about.html')


def delivery(request):
    """ A view to return the Delivery page """

    return render(request, 'delivery-info.html')


def returns(request):
    """ A view to return the Returns & Refunds page """

    return render(request, 'returns.html')
