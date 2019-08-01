from django.shortcuts import render, Http404
from django.http import HttpResponse
from django.db.models import Q
from .forms import FormBeli
from .models import Menu
from django.core.paginator import Paginator

def index(request):
    menus = Menu.objects.filter(kuantitas__gt=0)
    paginator = Paginator(menus, 3)
    context = {
        'title': 'Catalog',
        'subtitle': 'Catalog',
        'Menus': menus,

    }
    return render(request, 'menu/menu.html', context)

def indexCategory(request, category):
    menus = {}
    page = request.GET.get('page', 1)
    if category == 'pria':
        menus = Menu.objects.filter(Q(JK__iexact='pria') | Q(JK__iexact='semua'),kuantitas__gt=0, active=True).order_by('timestamp')
    elif category == 'wanita':
        menus = Menu.objects.filter(Q(JK__iexact='wanita') | Q(JK__iexact='semua'), kuantitas__gt=0, active=True).order_by('timestamp')
    else:
        menus = Menu.objects.filter(kuantitas__gt=0, active=True).order_by('timestamp').order_by('timestamp')
    
    paginator = Paginator(menus, 3)

    try:
        posts = paginator.page(page)
    except:
        pass
    context = {
        'title': 'Catalog',
        'subtitle': 'Catalog',
        'Menus': posts,
        # 'posts':posts,

    }
    return render(request, 'menu/menu.html', context)

def beli(request, category,slug):
    try:
        FormBelii = FormBeli()

        pilihan = Menu.objects.get(slug=slug)
        pilihann = Menu.objects.filter(
            slug=slug).values_list('judulMenu', 'hargaMenu')
    except:
        raise Http404
    context = {
        'title': 'Order',
        'subtitle': 'Orders Detail',
        'Menus': pilihan,
        'FormMenu': FormBelii,
    }
    return render(request, 'menu/beli.html', context)
