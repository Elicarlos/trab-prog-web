from django.shortcuts import render

from core.models import Produto

# Create your views here.
def index(request):
    produto = Produto.objects.all()
    print(produto)
    context = {
        'produto': produto
    }
    
    return render(request, 'index.html', context)





