from email import message
from string import Template
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactFrom
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.views.generic import TemplateView
from django.db.models import Q 
# Create your views here.

def home(request):
    categories = Category.objects.filter(c_status=True)
    products = Product.objects.filter(p_status=True).order_by('p_price')
    productrecommend = Product.objects.filter(p_recommend=True)
    sort_by = request.GET.get("sort", "l2h") 
    if sort_by == "l2h":
        products = Product.objects.filter(p_status=True).order_by("p_price")
        productrecommend = Product.objects.filter(p_recommend=True).order_by("p_price")
    elif sort_by == "h2l":
        products = Product.objects.filter(p_status=True).order_by("-p_price")
        productrecommend = Product.objects.filter(p_recommend=True).order_by("-p_price")


    cate_id = request.GET.get('category')
    if cate_id:
        products = products.filter(p_category_id=cate_id)

    paginator = Paginator(products, 8)
    pang = request.GET.get('page')
    try:
        products = paginator.page(pang)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {
        'categories': categories,
        'products': products,
        'cate_id': cate_id,
        'productrecommend': productrecommend,
    })


def productdetail(request, slug):
    product = get_object_or_404(Product, p_slug=slug)
    productrecommend = Product.objects.filter(p_recommend=True)
    category = Category.objects.all()
    return render(request, 'detail.html', {
        'product': product,
        'productrecommend': productrecommend,
        'categories':category,

    })

def contact(request):
    form = ContactFrom()
    category = Category.objects.all()
    if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'SUCCESS')
            form = ContactFrom()
            return HttpResponseRedirect(reverse('contact', kwargs={}))
        messages.error(request, 'Save failed')
        
    return render(request, 'contact.html', {
        'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY,
        'form': form,
        'categories':category,
    })

def search(request):
    category = Category.objects.all()
    kw = request.GET.get("key")
    if kw:
        searchproduct = Product.objects.filter(p_name=kw)
    else:
        searchproduct = Product.objects.all()
    print(kw)
    return render(request, 'search.html', {
        'searchproduct': searchproduct,
        'categories':category,
    })

#class SearchView(TemplateView):
#    template_name = 'search.html'
#    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        kw = self.request.GET.get("keyword")
#        results = Product.objects.filter(Q(p_name__icontains=kw))
#        print(results)
#        return context
