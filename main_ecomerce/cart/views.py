from django.shortcuts import render


# Create your views here.
def addtocart(request):
    if request.method == 'POST':
        return render(request, 'cart/cart.html')
