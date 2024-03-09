from django.shortcuts import render, redirect
from .models import Estoque
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader


def home(request):
    estoques = Estoque.objects.all() 
    print(estoques)
    return render(request, "index.html", {'estoques':estoques})

def salvar(request):
    if request.method == 'POST':
        quantidade = int(request.POST.get('Qtde'))
        valor_unitario = float(request.POST.get('Unitario'))
        
        valor_total = quantidade * valor_unitario
        
        novo_estoque = Estoque(
        Qtde=quantidade,
        Codigo=request.POST.get('Codigo'),
        Descricao=request.POST.get('Descricao'),
        Unitario=valor_unitario,
        Total=valor_total
    )
    
    novo_estoque.save()
    
    return redirect('home')


#def error404 (request, exception):
    #return render(request, '404.html')

#def error500 (request):
    #return render(request, '500.html')

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=500)