from django.shortcuts import render, redirect, get_object_or_404
from .models import Estoque
from django.http import HttpResponse
from django.template import loader

def index(request):
    #print(dir(request))
    estoques = Estoque.objects.all()
    return render(request, 'index.html', {'estoques': estoques})

def cadastro(request):
    estoques = Estoque.objects.all()
    return render(request, 'cadastro.html', {'estoques': estoques})


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
        return redirect('index')


def editar(request, id):
    instancia = get_object_or_404(Estoque, id=id)

    if request.method == 'POST':
        # Se o método for POST, significa que o formulário foi submetido
        quantidade = int(request.POST.get('Qtde'))
        valor_unitario = float(request.POST.get('Unitario'))
        valor_total = quantidade * valor_unitario
        
        instancia.Qtde = quantidade
        instancia.Codigo = request.POST.get('Codigo')
        instancia.Descricao = request.POST.get('Descricao')
        instancia.Unitario = valor_unitario
        instancia.Total = valor_total

        instancia.save()

        return redirect('index')
    else:
        # Se o método não for POST, significa que é uma solicitação GET para carregar o formulário de edição
        return render(request, 'editar.html', {'instancia': instancia})  
                     
def delete(request, id):
    instancia = get_object_or_404(Estoque, id=id)
    instancia.delete()   
    return redirect('index')  # Redireciona para a página de índice após a exclusão




def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=500)