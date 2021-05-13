from django.shortcuts import render,redirect
from .models import Product, Cart
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def register(request):
    if request.method == "POST":
        product_name = request.POST['Product_name']
        price = request.POST['price']
        product_Description = request.POST['Product_Description']
        full_Description = request.POST['Full_Description']
        gender = request.POST['gender']
        manufacturer = request.POST['Manufacturer']
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        product = Product(product_name=product_name, price=price, product_Description=product_Description, Gender=gender, Large_Description=full_Description, Manufacturer= manufacturer, image1=image1, image2= image2, image3= image3, image4=image4)
        product.save()
    return render(request, 'register.html')


def index(request):
    males = Product.objects.filter(Gender="male")[:4]
    females = Product.objects.filter(Gender="female")[:4]
    cart = Cart.objects.all()
    item = len(cart)
    males_footwear = {'males': males, 'females': females, 'cart':item}
    return render(request, 'index.html', males_footwear)


def about(request):
    cart = Cart.objects.all()
    item = len(cart)
    return render(request, 'about.html', {'cart':item})


def add_to_wishlist(request):
    cart = Cart.objects.all()
    item = len(cart)
    return render(request, 'add-to-wishlist.html', {'cart':item})


def cart(request):
    cart = Cart.objects.all()
    total_amount = 0
    print(cart)
    for i in cart:
        total_amount+= int(i.total_price)
    item = len(cart)
    return render(request, 'cart.html', {'item': cart, 'total_amount': total_amount, 'cart':item})


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def men(request):
    cart = Cart.objects.all()
    item = len(cart)
    males = Product.objects.filter(Gender="male")
    males_footwear = {'mens': males, 'cart':item}
    return render(request, 'men.html', males_footwear)


def order_complete(request):
    cart = Cart.objects.all()
    item = len(cart)
    return render(request, 'order-complete.html', {'cart': item})


def product_detail(request, sno):
    cart = Cart.objects.all()
    if request.method == 'POST':
        sno = request.POST['sno']
        product_name = request.POST['product_name']
        price = request.POST['price']
        number = request.POST['quantity']
        list = price.split(',')
        list = "".join(list)
        total_amount = int(list) * int(number)
        cart_data =Cart(product_sno=sno, number=number,product_name=product_name, price=price, total_price=total_amount)
        cart_data.save()
        return redirect('cart')
    product = Product.objects.get(sno=sno)
    item = len(cart)
    detail = {"product": product, 'cart':item}
    return render(request, 'product-detail.html', detail)


def women(request):
    cart = Cart.objects.all()
    item = len(cart)
    males = Product.objects.filter(Gender="female")
    females_footwear = {'females': males, 'cart':item}
    return render(request, 'women.html',females_footwear)
