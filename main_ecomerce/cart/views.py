from django.shortcuts import render


# Create your views here.
def add_to_cart(request):
    if request.method == 'POST':
        return render(request, 'cart/cart.html')
