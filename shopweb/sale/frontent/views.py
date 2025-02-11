from django.shortcuts import get_object_or_404, redirect, render
from system.models import Product, Category, CartItem
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.db.models import Q


# Create your views here.
def home(request):
    allsanpham = Product.objects.all()[:8]
    rau = Product.objects.filter(category_id = 7)[:8]
    traicay= Product.objects.filter(category_id = 8)[:8]
    banhmi= Product.objects.filter(category_id = 9)[:8]
    thit= Product.objects.filter(category_id = 10)[:8]
    sanphamupdate = Product.objects.all().order_by('-updated')[:6]
    passData = { 'all':allsanpham,'rau':rau,'traicay':traicay,'banhmi':banhmi,'thit':thit,'sanphamupdate':sanphamupdate}
    return render(request, 'frontent/home.html', passData)


# def shop(request):
#     allsanpham = Product.objects.all()
#     danhmuc = Category.objects.all()[:5]
#     fea=Product.objects.all().order_by('-updated')[:6]
#     listDanhmuc = Category.objects.all().prefetch_related('products')  
#     # phan trang
#     paginator = Paginator(allsanpham, 6)
#     pagenumber = request.GET.get('page')
#     spPage = paginator.get_page(pagenumber)
#     passData= {'all': spPage, 'danhmuc':danhmuc, 'fea':fea, 'listDanhmuc':listDanhmuc, }
#     return render(request, 'frontent/shop.html', passData)

def shop(request):
    allsanpham = Product.objects.all()
    danhmuc = Category.objects.all().order_by('-updated')[:5]
    fea = Product.objects.all().order_by('-updated')[:5]
    listDanhmuc = Category.objects.all().prefetch_related('products')
    search_query = request.GET.get('search', '')

    # Handle AJAX request for price filtering
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        max_price = float(request.GET.get('max_price', 10000000))
        filtered_products = Product.objects.filter(price__lte=max_price)

        #text search
        if search_query:
            filtered_products = filtered_products.filter(
                Q(name__icontains=search_query) |
                Q(decription__icontains=search_query) |
                Q(category__title__icontains=search_query)
            )
        
        # Paginate the filtered results
        paginator = Paginator(filtered_products, 9)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        context = {'all': page_obj}
        html = render_to_string('frontent/product_list.html', context)
        
        data = {
            'html': html,
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        }
        return JsonResponse(data)

    # Regular request
    phantrang = Paginator(allsanpham, 9)
    page_number = request.GET.get('page')
    spPage = phantrang.get_page(page_number)
    passData = {'all': spPage, 'danhmuc': danhmuc, 'fea': fea, 'listDanhmuc': listDanhmuc}
    return render(request, 'frontent/shop2.html', passData)




def detail(request, id):
    try:
        sanpham = Product.objects.get(id=id)
        lienquan = Product.objects.filter(category_id = sanpham.category_id)
        danhmuc = Category.objects.all()[:5]       
        fea=Product.objects.all().order_by('-updated')[:6]
        listDanhmuc = Category.objects.all().prefetch_related('products')       
        if lienquan:
            splienquan = lienquan
        else:
            splienquan = ""

        passData= {'sp': sanpham, 'splienquan':splienquan, 'danhmuc':danhmuc, 'fea':fea, 'listDanhmuc':listDanhmuc}
        
    except Product.DoesNotExist:
        return redirect('w.home')
    
    return render(request, 'frontent/detail.html', passData)
    

def contact(request):
    return render(request, 'frontent/contact.html')

@login_required(login_url='/secure/login/')
def cart(request):
    cart_item=CartItem.objects.filter(user=request.user)
    subtotal=sum(item.get_total_price() for item in cart_item) # 1 : hoa*1 = total , 2: cây*2=total
    ship=4.00
    total=subtotal+ship
    total_products = cart_item.count()
    passData={'cart_item':cart_item, 'subtotal':subtotal,'ship':ship,'total':total,'total_products':total_products}
    return render(request,'frontent/cart.html',passData)

@login_required(login_url='/secure/login/')
def remove_cart(request,id):
    cart_item=get_object_or_404(CartItem, id=id,user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('w.cart')


@login_required(login_url='/secure/login/')
def remove_cart_all(request,id):
    cart_item=get_object_or_404(CartItem, id=id,user=request.user)
    cart_item.delete()
    return redirect('w.cart')

@login_required(login_url='/secure/login/')
def add_cart(request,id):
    try:
        sp=Product.objects.get(id=id)
        cart_item,created=CartItem.objects.get_or_create(
            user=request.user,
            product=sp
        )
        if not created:
            cart_item.quantity +=1
            cart_item.save()
        return redirect('w.cart')    
    except Product.DoesNotExist:
        return redirect("w.home")
    

def checkout(request):
    return render(request, 'frontent/checkout.html')

def numcard(request):
    cart_item=CartItem.objects.filter(user=request.user)
    total_products = cart_item.count()
    passData={'total_products':total_products}
    return render(request, 'frontent/layout.html', passData)

def ajax(request):
    return render(request, 'frontent/ajax.html')





@csrf_exempt # Chỉ sử dụng trong ví dụ, không nên dùng trong production
def process_data(request):
    if request.method == 'POST':
        data = request.POST.get('data', '')
        name = request.POST.get('name', '')
        # Xử lý dữ liệu ở đây. Trong ví dụ này, chúng ta chỉ đảo ngược chuỗi
        # processed_data = data[::-1]
        return JsonResponse({'result': data, 'name': name})
    return JsonResponse({'error': 'Invalid request method'})