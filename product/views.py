from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
# from user.models import User
from .models import Product
# from .models import User

def home(request):
    return render(request, 'index.html')

def pageone(request):
    return render(request, 'Pageone.html')

def pagetwo(request):
    return render(request, 'Pagetwo.html')

def pagethree(request):
    return render(request, 'Pagethree.html')

def pagefour(request):
    return render(request, 'Pagefour.html')

def pagefive(request):
    return render(request, 'Pagefive.html')

def basket(request):
    return render(request, 'basket.html')

def pageonedetail(request):
    return render(request, 'Page1_detail.html')

def pagetwodetail(request):
    return render(request, 'Page2_detail.html')

def pagethreedetail(request):
    return render(request, 'Page3_detail.html')

def pagefourdetail(request):
    return render(request, 'Page4_detail.html')

def pagefivedetail(request):
    return render(request, 'Page5_detail.html')

def success(request):
    return render(request, 'success.html')

def product_list(request):
    if request.method == 'GET':

        all_product = Product.objects.all().order_by('-id')
        page = int(request.GET.get('p', 1))
        paginator = Paginator(all_product, 3)
        pages = paginator.get_page(page)
        return render(request, 'product/list/.html')


def prodcut_write(request):

    if request.method == 'POST':
        if not request.session.get('user'):
            return redirect('/user/login/')

        else:
            request.method == 'POST'
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)
            product = Product()
            product.title = request.POST['title']
            product.contents = request.POST['contents']
            product.writer = user
            product.save()

            return redirect('product/write/.html')


def product_detail(request, pk):
    if request.method == 'GET':
        try:
            page = Product.objects.get(pk=pk)

        except Product.DoesNotExist:
            raise Http404('게시글을 찾을수 없습니다')

        return render(request, 'product_detail.html', {'page': page})
