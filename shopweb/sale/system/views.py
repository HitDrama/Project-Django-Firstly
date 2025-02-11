from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Config
from .forms import CategoryForm, ProductForm, UserForm, ConfigForm
from django.contrib.auth.decorators import login_required
from secure.models import CustomUser
from django.contrib import messages

# Create your views here.

def manager(request):
    return render(request, 'system/manager/manager.html')

def account(request):
    list=CustomUser.objects.all()
    return render(request, 'system/account/list.html',{'account':list})
def add_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm tài khoản thành công')
            return redirect('s.account')
    else:
        form = UserForm()
    return render(request, 'system/account/form.html', {'form': form})
def edit_account(request, id):  # Cập nhật hàm edit_account để nhận tham số id
    acc = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=acc)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật tài khoản thành công')
            return redirect('s.account')
    else:
        form = UserForm(instance=acc)
    return render(request, 'system/account/form.html', {'form': form})

def del_account(request,id):
    acc=get_object_or_404(CustomUser, id=id)
    acc.delete()
    messages.success(request, 'Xóa tài khoản thành công')
    return redirect('s.account')

def category(request):
    categories = Category.objects.all()
    return render(request, 'system/category/list.html', {'cate': categories})

def add_category(request):
    if request.method == 'POST':
        formdm = CategoryForm(request.POST, request.FILES)
        if formdm.is_valid():
            formdm.save()
            return redirect('s.category')
    else:
        formdm = CategoryForm()    
        return render(request, 'system/category/form.html', {'form': formdm})
    
def del_category(request, id):
    cate = get_object_or_404(Category, id=id)
    cate.delete()
    return redirect('s.category')

def edit_category(request, id):
    if request.method == 'POST':
        cate = get_object_or_404(Category, id=id)
        formdm = CategoryForm(request.POST, request.FILES, instance=cate)
        if formdm.is_valid():
            formdm.save()
            return redirect('s.category')
    else:
        cate = get_object_or_404(Category, id=id)
        formdm = CategoryForm(instance=cate)
        return render(request, 'system/category/form.html', {'form': formdm})



#quan ly san pham
def product(request):
    products = Product.objects.all() # tuong duong voi select * from product
    return render(request, 'system/product/list.html',{'sp' : products})

def add_product(request):
    if request.method == 'POST':
        formsp = ProductForm(request.POST, request.FILES)
        if formsp.is_valid():
            formsp.save()
            return redirect('s.product')
    else:
        formsp = ProductForm()
        return render(request, 'system/product/form.html', {'form': formsp})
    

def del_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('s.product')

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        formsp = ProductForm(request.POST, request.FILES, instance=product)
        if formsp.is_valid():
            formsp.save()
            return redirect('s.product')
    else:       
        formsp = ProductForm(instance=product)
        return render(request, 'system/product/form.html', {'form': formsp})
    
#bao-tri
def config(request):
    cauhinh = Config.objects.first()
    config = get_object_or_404(Config, id=cauhinh.id)
    if request.method == 'POST':
        form = ConfigForm(request.POST, request.FILES, instance=config)
        if form.is_valid():
            form.save()
            return redirect('s.config')
    else:       
        form = ConfigForm(instance=config)
        return render(request, 'system/manager/config.html', {'form': form})
