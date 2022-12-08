from django.shortcuts import render


def contact(request):
    """ A view to return the Contact Us page """

    return render(request, 'contact/contact.html')


def about(request):
    """ A view to return the About Us page """

    return render(request, 'contact/about.html')


def delivery(request):
    """ A view to return the Delivery Info page """

    return render(request, 'contact/delivery-info.html')


def returns(request):
    """ A view to return the Returns & Refunds page """

    return render(request, 'contact/returns.html')
