from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from core.forms import EstudianteForm
from core.models import Estudiante
from core.forms import FamiliaForm,EnfermedadForm,RetiroForm,FormularioForm
from core.models import Familia,Enfermedad,Retiro,Formulario
from core.forms import Estudiante_Familia_Enfermedad_Formulario_RetiroForm,CursoForm
from core.models import Estudiante_Familia_Enfermedad_Formulario_Retiro,Curso

@login_required(None,"",'login')
def portada(request, plantilla="portada.html"):
    return render(request, plantilla);

@login_required(None,"",'login')
def MyV(request, plantilla="MyV.html"):
    return render(request, plantilla);

@login_required(None,"",'login')
def crearcurso(request):
    if request.method=='POST':
        cursoForm = CursoForm(request.POST)
        if cursoForm.is_valid():
            cursoForm.save()
            return redirect('curso')
    else:
        cursoForm = CursoForm()
    return render(request,'crearcurso.html',{'cursoform':cursoForm})

@login_required(None,"",'login')
def curso (request):
    curso = list(Curso.objects.all())
    return render(request, 'curso.html',{'curso' : curso})

@login_required(None,"",'login')
def modificarcurso(request, pk):
    if request.method == "POST":
        curso = get_object_or_404(Curso, pk=pk)
        cursoForm = CursoForm (request.POST or None, instance=curso)
        if cursoForm.is_valid():
            cursoForm.save()
        return redirect("curso")
    else:
        curso = get_object_or_404(Curso, pk=pk)
        cursoForm = CursoForm(request.POST or None, instance=curso)
    return render(request, 'modificarcurso.html', {'cursoform':cursoForm})

@login_required(None,"",'login')
def eliminarcurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('curso')

@login_required(None,"",'login')
def crearestudiante(request,plantilla='crearestudiante.html'):
    if request.method=='POST':
        estudianteForm = EstudianteForm(request.POST)
        if estudianteForm.is_valid():
            estudianteForm.save()
            return redirect('estudiantes')
    else:
        estudianteForm = EstudianteForm()
    return render(request,plantilla,{'estudianteform':estudianteForm})

@login_required(None,"",'login')
def estudiantes (request, plantilla="estudiantes.html"):
    estudiantes = list(Estudiante.objects.all())
    return render(request, plantilla,{'estudiantes' : estudiantes})

@login_required(None,"",'login')
def modificarestudiante(request, pk, plantilla="modificarestudiante.html"):
    if request.method == "POST":
        estudiante = get_object_or_404(Estudiante, pk=pk)
        estudianteForm = EstudianteForm(request.POST or None, instance=estudiante)
        if estudianteForm.is_valid():
            estudianteForm.save()
        return redirect("estudiantes")
    else:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        estudianteForm = EstudianteForm(request.POST or None, instance=estudiante)
    return render(request, plantilla, {'estudianteform':estudianteForm})

@login_required(None,"",'login')
def eliminarestudiante(request, pk, plantilla="eliminarestudiante.html"):
    if request.method == "POST":
        estudiante = get_object_or_404(Estudiante, pk=pk)
        estudianteForm = EstudianteForm(request.POST or None, instance=estudiante)
        if estudianteForm.is_valid():
            estudiante.delete()
        return redirect("estudiantes")
    else:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        estudianteForm = EstudianteForm(request.POST or None, instance=estudiante)
    return render(request, plantilla, {'estudianteform':estudianteForm})

@login_required(None,"",'login')
def crearfamilia(request,plantilla='crearfamilia.html'):
    if request.method=='POST':
        familiaForm = FamiliaForm(request.POST)
        if familiaForm.is_valid():
            familiaForm.save()
            return redirect('familia')
    else:
        familiaForm = FamiliaForm()
    return render(request,plantilla,{'familiaform':familiaForm})

@login_required(None,"",'login')
def familia (request, plantilla="familia.html"):
    familias = list(Familia.objects.all())
    return render(request, plantilla,{'familias' : familias})

@login_required(None,"",'login')
def modificarfamilia(request, pk, plantilla="modificarfamilia.html"):
    if request.method == "POST":
        familia = get_object_or_404(Familia, pk=pk)
        familiaForm = FamiliaForm(request.POST or None, instance=familia)
        if familiaForm.is_valid():
            familiaForm.save()
        return redirect("familia")
    else:
        familia = get_object_or_404(Familia, pk=pk)
        familiaForm = FamiliaForm(request.POST or None, instance=familia)
    return render(request, plantilla, {'familiaform':familiaForm})

@login_required(None,"",'login')
def eliminarfamilia(request, pk, plantilla="eliminarfamilia.html"):
    if request.method == "POST":
        familia = get_object_or_404(Familia, pk=pk)
        familiaForm = FamiliaForm(request.POST or None, instance=familia)
        if familiaForm.is_valid():
            familia.delete()
        return redirect("familia")
    else:
        familia = get_object_or_404(Familia, pk=pk)
        familiaForm = FamiliaForm(request.POST or None, instance=familia)
    return render(request, plantilla, {'familiaform':familiaForm})

@login_required(None,"",'login')
def crearenfermedad(request,plantilla='crearenfermedad.html'):
    if request.method=='POST':
        enfermedadForm = EnfermedadForm(request.POST)
        if enfermedadForm.is_valid():
            enfermedadForm.save()
            return redirect('enfermedades')
    else:
        enfermedadForm = EnfermedadForm()
    return render(request,plantilla,{'enfermedadform':enfermedadForm})
@login_required(None,"",'login')
def modificarenfermedad(request, pk, plantilla="modificarenfermedad.html"):
    if request.method == "POST":
        enfermedad = get_object_or_404(Enfermedad, pk=pk)
        enfermedadForm = EnfermedadForm(request.POST or None, instance=enfermedad)
        if enfermedadForm.is_valid():
            enfermedadForm.save()
        return redirect("enfermedades")
    else:
        enfermedad = get_object_or_404(Enfermedad, pk=pk)
        enfermedadForm = EnfermedadForm(request.POST or None, instance=enfermedad)
    return render(request, plantilla, {'enfermedadform':enfermedadForm})

@login_required(None,"",'login')
def enfermedades (request, plantilla="enfermedades.html"):
    enfermedades = list(Enfermedad.objects.all())
    return render(request, plantilla,{'enfermedades' : enfermedades})

@login_required(None,"",'login')
def eliminarenfermedad(request, pk, plantilla="eliminarenfermedad.html"):
    if request.method == "POST":
        enfermedad = get_object_or_404(Enfermedad, pk=pk)
        enfermedadForm = EnfermedadForm(request.POST or None, instance=enfermedad)
        if enfermedadForm.is_valid():
            enfermedad.delete()
        return redirect("enfermedades")
    else:
        enfermedad = get_object_or_404(Enfermedad, pk=pk)
        enfermedadForm = EnfermedadForm(request.POST or None, instance=enfermedad)
    return render(request, plantilla, {'enfermedadform':enfermedadForm})

@login_required(None,"",'login')
def crearretiro(request,plantilla='crearretiro.html'):
    if request.method=='POST':
        retiroForm = RetiroForm(request.POST)
        if retiroForm.is_valid():
            retiroForm.save()
            return redirect('retiro')
    else:
        retiroForm = RetiroForm()
    return render(request,plantilla,{'retiroform':retiroForm})

@login_required(None,"",'login')
def modificarretiro(request, pk, plantilla="modificarretiro.html"):
    if request.method == "POST":
        retiro = get_object_or_404(Retiro, pk=pk)
        retiroForm = RetiroForm(request.POST or None, instance=retiro)
        if retiroForm.is_valid():
            retiroForm.save()
        return redirect("retiro")
    else:
        retiro = get_object_or_404(Retiro, pk=pk)
        retiroForm = RetiroForm(request.POST or None, instance=retiro)
    return render(request, plantilla, {'retiroform':retiroForm})

@login_required(None,"",'login')
def retiro (request, plantilla="Retiro.html"):
    retiros = list(Retiro.objects.all())
    return render(request, plantilla,{'retiros' : retiros})

@login_required(None,"",'login')
def eliminarretiro(request, pk, plantilla="eliminarretiro.html"):
    if request.method == "POST":
        retiro = get_object_or_404(Retiro, pk=pk)
        retiroForm = RetiroForm(request.POST or None, instance=retiro)
        if retiroForm.is_valid():
            retiro.delete()
        return redirect('retiro')
    else:
        retiro = get_object_or_404(Retiro, pk=pk)
        retiroForm = RetiroForm(request.POST or None, instance=retiro)
    return render(request, plantilla, {'retiroform':retiroForm})

@login_required(None,"",'login')
def crearformulario(request,plantilla="crearformulario.html"):
    if request.method=='POST':
        formularioForm = FormularioForm(request.POST)
        if formularioForm.is_valid():
            formularioForm.save()
            return redirect('formulario')
    else:
        formularioForm = FormularioForm()
    return render(request,plantilla,{'formularioform':formularioForm})

@login_required(None,"",'login')
def formulario (request, plantilla="formulario.html"):
    formularios = list(Formulario.objects.all())
    return render(request, plantilla,{'formularios' : formularios})

def modificarformulario(request, pk, plantilla="modificarformulario.html"):
    if request.method == "POST":
        formulario = get_object_or_404(Formulario, pk=pk)
        formularioForm = FormularioForm(request.POST or None, instance=formulario)
        if formularioForm.is_valid():
            formularioForm.save()
        return redirect("formulario")
    else:
        formulario = get_object_or_404(Formulario, pk=pk)
        formularioForm = FormularioForm(request.POST or None, instance=formulario)
    return render(request, plantilla, {'formularioform':formularioForm})

@login_required(None,"",'login')
def eliminarformulario(request, pk, plantilla="eliminarformulario.html"):
    if request.method == "POST":
        formulario = get_object_or_404(Formulario, pk=pk)
        formularioForm = FormularioForm(request.POST or None, instance=formulario)
        if formularioForm.is_valid():
            formulario.delete()
        return redirect("formulario")
    else:
        formulario = get_object_or_404(Formulario, pk=pk)
        formularioForm = FormularioForm(request.POST or None, instance=formulario)
    return render(request, plantilla, {'formularioform':formularioForm})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
@login_required(None,"",'login')
def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/welcome')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})



@login_required(None,"",'login')
def creargeneral(request,plantilla='creargeneral.html'):
    if request.method=='POST':
        estudiante_familia_enfermedad_formulario_retiroForm = Estudiante_Familia_Enfermedad_Formulario_RetiroForm(request.POST)
        if estudiante_familia_enfermedad_formulario_retiroForm.is_valid():
            estudiante_familia_enfermedad_formulario_retiroForm.save()
            return redirect('general')
    else:
        estudiante_familia_enfermedad_formulario_retiroForm = Estudiante_Familia_Enfermedad_Formulario_RetiroForm()
    return render(request,plantilla,{'estudiante_familia_enfermedad_formulario_retiroform':estudiante_familia_enfermedad_formulario_retiroForm})

@login_required(None,"",'login')
def general (request, plantilla="general.html"):
    estudiantes_familias_enfermedades_formularios_retiros = list(Estudiante_Familia_Enfermedad_Formulario_Retiro.objects.all())
    return render(request, plantilla,{'estudiantes_familias_enfermedades_formularios_retiros' : estudiantes_familias_enfermedades_formularios_retiros})

@login_required(None,"",'login')
def modificargeneral(request, pk, plantilla="modificargeneral.html"):
    if request.method == "POST":
        estudiante_familia_enfermedad_formulario_retiro = get_object_or_404(Estudiante_Familia_Enfermedad_Formulario_Retiro, pk=pk)
        estudiante_familia_enfermedad_formulario_retiroForm = Estudiante_Familia_Enfermedad_Formulario_RetiroForm(request.POST or None, instance=estudiante_familia_enfermedad_formulario_retiro)
        if estudiante_familia_enfermedad_formulario_retiroForm.is_valid():
            estudiante_familia_enfermedad_formulario_retiroForm.save()
        return redirect("general")
    else:
        estudiante_familia_enfermedad_formulario_retiro = get_object_or_404(Estudiante_Familia_Enfermedad_Formulario_Retiro, pk=pk)
        estudiante_familia_enfermedad_formulario_retiroForm = Estudiante_Familia_Enfermedad_Formulario_RetiroForm(request.POST or None, instance=estudiante_familia_enfermedad_formulario_retiro)
    return render(request, plantilla, {'estudiante_familia_enfermedad_formulario_retiroform':estudiante_familia_enfermedad_formulario_retiroForm})

@login_required(None,"",'login')
def eliminargeneral(request, pk, plantilla="eliminargeneral.html"):
    if request.method == "POST":
        estudiante_familia_enfermedad_formulario_retiro = get_object_or_404(Estudiante_Familia_Enfermedad_Formulario_Retiro, pk=pk)
        estudiante_familia_enfermedad_formulario_retiroForm = Estudiante_Familia_Enfermedad_Formulario_RetiroForm(request.POST or None, instance=estudiante_familia_enfermedad_formulario_retiro)
        if estudiante_familia_enfermedad_formulario_retiroForm.is_valid():
            estudiante_familia_enfermedad_formulario_retiro.delete()
        return redirect("general")
    else:
        estudiante_familia_enfermedad_formulario_retiro = get_object_or_404(Estudiante_Familia_Enfermedad_Formulario_Retiro, pk=pk)
        estudiante_familia_enfermedad_formulario_retiroForm = Estudiante_Familia_Enfermedad_Formulario_RetiroForm(request.POST or None, instance=estudiante_familia_enfermedad_formulario_retiro)
    return render(request, plantilla, {'estudiante_familia_enfermedad_formulario_retiroform':estudiante_familia_enfermedad_formulario_retiroForm})