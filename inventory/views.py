from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import SupplierForm

def is_admin(user):
    return user.is_superuser

@login_required
def dashboard(request): any

@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def add_product(request): any

@login_required
@user_passes_test(is_admin)
def edit_product(request, id): any

@login_required
@user_passes_test(is_admin)
def delete_product(request, id): any

def is_admin(user):
    return user.is_superuser

def is_staff_user(user):
    return user.is_staff

@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def add_supplier(request):
    form = SupplierForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('add_product')  # back to product form

    return render(request, 'supplier_form.html', {'form': form})

# Dashboard + Search
def dashboard(request):
    query = request.GET.get('q')
    
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'dashboard.html', {'products': products})


# Add Product
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'form.html', {'form': form})


# Edit Product
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'form.html', {'form': form})


# Delete Product
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('dashboard')


# Report + Chart Data
def report(request):
    total_products = Product.objects.count()
    low_stock = Product.objects.filter(quantity__lt=10).count()
    healthy = total_products - low_stock

    products = Product.objects.all()
    names = [p.name for p in products]
    quantities = [p.quantity for p in products]

    return render(request, 'report.html', {
        'total': total_products,
        'low': low_stock,
        'healthy': healthy,
        'names': names,
        'quantities': quantities
    })