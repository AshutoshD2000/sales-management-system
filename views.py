from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Sale
def home(request):
    return render(request, 'home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def home(request):
    from .models import Product, Sale

    total_products = Product.objects.count()
    total_sales = Sale.objects.count()

    return render(request, 'home.html', {
        'total_products': total_products,
        'total_sales': total_sales
    })






def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']

        Product.objects.create(name=name, price=price, quantity=quantity)
        return redirect('/products/')

    return render(request, 'add_product.html')


def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales_list.html', {'sales': sales})


def add_sale(request):
    products = Product.objects.all()

    if request.method == "POST":
        product_id = request.POST['product']
        quantity_sold = int(request.POST['quantity'])

        product = Product.objects.get(id=product_id)

        total_price = product.price * quantity_sold

        # update stock
        product.quantity -= quantity_sold
        product.save()

        Sale.objects.create(
            product=product,
            quantity_sold=quantity_sold,
            total_price=total_price
        )

        return redirect('/sales/')

    return render(request, 'add_sale.html', {'products': products})