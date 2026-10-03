from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required  # <- Importar aquí
from .models import Persona

# aqui
@login_required  # <- Proteger la vista
def lista_personas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        celular = request.POST.get('celular')
        foto = request.FILES.get('foto')
        if nombre and celular and foto:
            Persona.objects.create(nombre=nombre, celular=celular, foto=foto)
        return redirect('lista_personas')

    por_pagina = request.GET.get('page_size', 10)
    try:
        por_pagina = int(por_pagina)
        if por_pagina not in [10, 100]:
            por_pagina = 10
    except ValueError:
        por_pagina = 10

    personas_list = Persona.objects.all().order_by('-fecha_creacion')
    paginator = Paginator(personas_list, por_pagina)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'carnets_app/index.html', {
        'page_obj': page_obj,
        'por_pagina': por_pagina
    })
# fin

def lista_personas(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        celular = request.POST.get('celular')
        foto = request.FILES.get('foto')
        if nombre and celular and foto:
            Persona.objects.create(nombre=nombre, celular=celular, foto=foto)
        return redirect('lista_personas')

    # Control de paginación (10 o 100 por página)
    por_pagina = request.GET.get('page_size', 10)
    try:
        por_pagina = int(por_pagina)
        if por_pagina not in [10, 100]:
            por_pagina = 10
    except ValueError:
        por_pagina = 10

    personas_list = Persona.objects.all().order_by('-fecha_creacion')
    paginator = Paginator(personas_list, por_pagina)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'carnets_app/index.html', {
        'page_obj': page_obj,
        'por_pagina': por_pagina
    })