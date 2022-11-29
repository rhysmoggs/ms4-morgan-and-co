from django.shortcuts import render


def about(request):
    """ A view to return the About Us page """

    return render(request, 'info/about.html')


def delivery(request):
    """ A view to return the Delivery Info page """

    return render(request, 'info/delivery-info.html')


def returns(request):
    """ A view to return the Returns & Refunds page """

    return render(request, 'info/returns.html')
