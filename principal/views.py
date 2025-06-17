from django.shortcuts import render

def bienvenida(request):
    return render(request, 'principal/bienvenida.html')

def servicios(request):
    return render(request, 'principal/servicios.html')

def dinamico(request):
    # Placeholder para contenido dinámico futuro
    return render(request, 'principal/dinamico.html')