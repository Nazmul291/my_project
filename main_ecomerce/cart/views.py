from django.shortcuts import render


# Create your views here.
def addToCart(request):
    if request.method == 'POST':
        return render(request, 'cart/cart.html')
