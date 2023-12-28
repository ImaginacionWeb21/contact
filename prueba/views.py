from django.shortcuts import render,HttpResponse
from .form import ContactoForm


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        nombre= request.POST.get('nombre')
        correo= request.POST.get('correo')
        mensaje= request.POST.get('mensaje')

        print('nombre:',nombre)
        print('Email:',correo)
        print('mensaje:',mensaje)
        if form.is_valid():
            form.save()


    else:
        form = ContactoForm()

    return render(request,'prueba/index.html')
