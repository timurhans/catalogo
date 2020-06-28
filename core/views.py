from django.shortcuts import render
from django.http import HttpResponse
import glob
from .models import (Page,Like)

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def catalogo_view(request,cnpj):

    ip = get_client_ip(request)

    if request.method == 'POST':
        qs = request.POST
        for key,value in qs.items():
            if key.startswith("chk"):
                #caso o item no formulario esteja marcado, valores sao setados para True
                Like.objects.filter(cnpj=cnpj,ip=ip,page__ordem=value).update(liked=True)
        return HttpResponse('<script>history.back();</script>')

    #consulta os objetos Like para aquele ip e cnpj
    likes = Like.objects.filter(cnpj=cnpj).filter(ip=ip).order_by('page__ordem')

    #se nao existem Like objects com ip e cnpj cria para todas as paginas
    if len(likes)==0:
        pages = Page.objects.all().order_by('ordem')
        for page in pages:
            Like.objects.create(cnpj=cnpj,ip=ip,page=page)
        likes = Like.objects.filter(cnpj=cnpj).filter(ip=ip).order_by('page__ordem')

    for like in likes:
        if like.page.img.path.endswith('mp4'):
            like.page.tipo = 'video'
        else:
            like.page.tipo = 'img'

    context = {
        'likes' : likes
    }
    return render(request,"catalogo.html",context)

def catalogo_basic_view(request):

    

    if request.method == 'POST':
        qs = request.POST
        ip = get_client_ip(request)
        for key,value in qs.items():
            if key.startswith("chk"):
                page = Page.objects.filter(ordem=value)[0]
                Like.objects.create(cnpj=cnpj,ip=ip,page=page)
        return HttpResponse('<script>history.back();</script>')

    pages = Page.objects.all().order_by('ordem')
    print(pages[0].img)
    context = {
        'pages' : pages
    }
    return render(request,"catalogo.html",context)