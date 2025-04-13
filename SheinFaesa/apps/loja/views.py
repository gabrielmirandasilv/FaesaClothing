from django.shortcuts import render

# Create your views here.

def exemplo(request):
    return render(request, "exemplo_loja/index.html")