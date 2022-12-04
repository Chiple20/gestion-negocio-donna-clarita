from django.db import IntegrityError
from django.shortcuts import render,redirect,HttpResponse
from .models import Usuario,Rol,Sucursal
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from GNDC import settings
from django.conf import settings
import pandas as pd
import random 
import numpy as np
#para los popup
from django.contrib import messages
#preddicion
from joblib import load
# Create your views here.

link="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.jetbrains.com%2Fhelp%2Fpycharm%2Fmanaging-dependencies.html&psig=AOvVaw2wHDclnYfF8iNUeGfT5QAN&ust=1666879021324000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCIC33rGG_voCFQAAAAAdAAAAABAE"

@login_required
def index(request):
    print("INDEX")
    context ={}
    return render(request, 'usuarios/index.html', context)

@login_required
def predicción(request):
    variables = [
                "Año",
                "Mes"
            ]
    if request.method == "GET":
        contexto = {
            "variables": variables
        }
        return render(request,'usuarios/prediccion.html', contexto)
    elif request.method == "POST":
        valores_formulario = []
        datos = "."
        for var in variables:
            dat= str(request.POST.get(var))
            datos = datos + dat
        datos=str(datos).replace(".","")
        datos=int(datos)
        print(datos)
        valores_formulario.append(datos)
        mejor_modelo = load(settings.RUTA_MODELO)
        prediccion=pd.DataFrame(valores_formulario)
        resultado = mejor_modelo.predict(prediccion)
        final=(np.round(resultado)).astype('int')
        final=str(final).replace("[","")
        final=str(final).replace("]","")
        final="{:,}".format(int(final))
        final=str("$"+final).replace(",",".")
      
        print(resultado)

        contexto = {
            "variables": variables,
            "resultado":final
        }
        return render(request,'usuarios/prediccion.html', contexto)

@login_required
def pred2(request):
    variables = [
                "Nom_productos",
                "IPC",
                "Precio",
                "Año",
                "Mes"
            ]
    for i in range(1,13):
        print("<option value='",i,"'>",i,"</option>")
    if request.method == "GET":
        contexto = {
            "variables": variables
        }
        return render(request,'usuarios/prediccion_2.html', contexto)
    elif request.method == "POST":
        valores_formulario = []
        for var in variables:
            valores_formulario.append(request.POST.get(var))
        mejor_modelo = load(settings.RUTA_MODELO2)
        print(valores_formulario)
        prediccion=pd.DataFrame([valores_formulario])
        resultado = mejor_modelo.predict(prediccion)
        final=(np.round(resultado)).astype('int')
        final=str(final).replace("[","")
        final=str(final).replace("]","")
        final="{:,}".format(int(final))
        final=str("$"+final).replace(",",".")
      
        print(final)
      
        print(resultado)

        contexto = {
            "variables": variables,
            "resultado":final
        }
        return render(request,'usuarios/prediccion_2.html', contexto)

@login_required        
def pred3(request):
    variables = [
                "Categoria",
                "Año",
                "Mes"
            ]
    if request.method == "GET":
        contexto = {
            "variables": variables
        }
        return render(request,'usuarios/prediccion_3.html', contexto)
    elif request.method == "POST":
        valores_formulario = []
        for var in variables:
            valores_formulario.append(request.POST.get(var))
        mejor_modelo = load(settings.RUTA_MODELO3)
        print(valores_formulario)
        prediccion=pd.DataFrame([valores_formulario])
        resultado = mejor_modelo.predict(prediccion)
        final=(np.round(resultado)).astype('int')
        final=str(final).replace("[","")
        final=str(final).replace("]","")
        final="{:,}".format(int(final))
        final=str(final).replace(","," ")
      
        print(final)
      
        print(resultado)

        contexto = {
            "variables": variables,
            "resultado":final
        }
        return render(request,'usuarios/prediccion_3.html', contexto)

@login_required
def dashboard(request):
    print("INDEX")
    context ={}
    return render(request, 'usuarios/dashboard.html',context)  

#crud 
@login_required
def Modificar(request):
    print("Modificar")
    context ={}
    return render(request, 'usuarios/Modificar.html', context)

@login_required
def Eliminar(request):
    print("Eliminar")
    listaUsuarios =Usuario.objects.all()
    return render(request, 'usuarios/Eliminar.html',{"usuarios":listaUsuarios}) 
@login_required
def Añadir(request):
    print("Modificar")
    context ={}
    return render(request, 'usuarios/Añadir.html',context)

def Listado(request):
    print("Ingreso al listado")
    listaUsuarios =Usuario.objects.all()
    return render(request, 'usuarios/Listado.html',{"usuarios":listaUsuarios})
#################################################################       

#PERFIL
@login_required
def Perfil(request):
    print("Añadir")
    context ={}
    return render(request, 'usuarios/Perfil.html', context)

@login_required
def Password(request):
    context ={}
    if request.method == "GET":
        return render(request, 'usuarios/password.html', context)
        
    elif request.method == "POST":
        try:
            Gmail = request.POST['Mail']
            print(request.POST['passA'])
            print(request.POST['pass1'])
            print(request.POST['pass2'])
            u = Usuario.objects.get(email=Gmail)
            if u.check_password(request.POST['passA']) == True:
                if request.POST['pass1'] == request.POST['pass2']:
                    u.set_password(request.POST['pass2'])
                    u.save() 
                    return redirect(to=Perfil)
                else:
                    messages.error(request,"Sus Contraseñas no coinciden") 
                    print("salio mal")
                    return render(request, 'usuarios/password.html', context)

            else:
                messages.error(request,"Su Contraseña es incorrecta") 
                print("salio mal")
                return render(request, 'usuarios/password.html', context)

        except IntegrityError as e:
            messages.error(request,"No se pudo cambiar su contraseña") 
            print("salio mal")
            return render(request, 'usuarios/password.html', context)

def borraUsuarios(request):
    print("borraUsuarios")
    listaUsuarios =Usuario.objects.all()
    return render(request, 'usuarios/borraUsuarios.html',{"usuarios":listaUsuarios})

def gestionUsuarios(request):
    print("gestionUsuarios")
    listaUsuarios =Usuario.objects.all()
    return render(request, 'usuarios/gestionUsuarios.html',{"usuarios":listaUsuarios})

#Crud Usuario
@login_required
def AgregarUsuario(request):
    #generador de pass
    minus   ="abcdefghijklmnopqrstuvwyxz"
    mayus   ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num     ="0123456789"
    simb    =",.-_"

    todos = minus + mayus + num +simb
    largo = 8
    genPass = "".join(random.sample(todos,largo))
    print(genPass)

    print("Agregando usuario")
    if request.method == 'POST':
        # sucursal = Sucursal()
        Vnombre= request.POST['innombre']
        print(Vnombre)
        Vapellido=  request.POST['inapellido']
        Vpassword=  genPass
        Vcorreo=    request.POST['incorreo']
        Vlink =     request.POST['inlink']
        VOPuser =   "False"
        Vrol= Rol.objects.get(id_rol =  request.POST['inrol'])
        print(Vrol)
        Vsucursal= Sucursal.objects.get(id_sucursal =  request.POST['insucursal'])
        print(Vsucursal)
        if Vcorreo != "":
            try:
               print("try")
               
               usuario = Usuario()
               usuario.username         = Vnombre
               usuario.last_name        = Vapellido 
               usuario.password         = make_password(Vpassword)
               usuario.email            = Vcorreo
               usuario.link             = Vlink
               usuario.is_superuser     = VOPuser
               usuario.id_rol           = Vrol
               usuario.id_sucursal      = Vsucursal
               print(usuario)
               print("holas")
               usuario.save()
               print("adios")
               print(usuario)
               template = get_template('usuarios/Correo.html')
               # Se renderiza el template y se envias parametros
               print('template')
               content = template.render({'email': Vcorreo,'contraseña':Vpassword})
               print('template2')
               # Se crea el correo (titulo, mensaje, emisor, destinatario)
               msg = EmailMultiAlternatives('Contraseña de usuario','Le enviamos la contraseña de usuario',settings.EMAIL_HOST_USER,[Vcorreo])
               msg.attach_alternative(content, 'text/html')
               msg.send()
               messages.success(request,"Se guardo al usuario correctamente")
               return render( request,'usuarios/Añadir.html',{})

            except IntegrityError as e:
               print("el error")
               print(e)
               messages.error(request,"No se pudo guardar el usuario") 
               return render(request, 'usuarios/Añadir.html', {})
        else:
            messages.error(request,"Este Usuario ya existe") 
            return render(request, 'usuarios/Añadir.html', {})
    else:
        messages.error(request,"No se pudo guardar el usuario") 
        return render(request, 'usuarios/Añadir.html', {})


################# buscador listado
@login_required
def buscador(request):
    if request.method == 'POST':
            buscaUsuario = request.POST['buscar']
            print(buscaUsuario)
            if buscaUsuario != "":
                try:
                    usuario = Usuario.objects.all()
                    usuario = Usuario.objects.filter(
                        Q(username__icontains = buscaUsuario) |
                        Q(last_name__icontains = buscaUsuario)|
                        Q(email__icontains = buscaUsuario)
                        ).distinct()
                    print(usuario)
                    if usuario is not None:
                        print("usuario =", usuario)
                        return render(request, 'usuarios/Listado.html', {"usuarios":usuario})
                    else:
                        return render(request, 'usuarios/Listado.html',{})
                except usuario.DoesNotExist:
                    return render(request, 'usuarios/Listado.html', {})
            else:
                return render(request, 'usuarios/Listado.html', {})
    else:
        return render(request, 'usuarios/Listado.html', {})
        
################# buscador de eliminar
@login_required
def buscaLista(request):
    if request.method == 'POST':
            buscaUsuario = request.POST['buscar']
            print(buscaUsuario)
            if buscaUsuario != "":
                try:
                    usuario = Usuario.objects.all()
                    usuario = Usuario.objects.filter(Q(email = buscaUsuario))
                    print(usuario)
                    if usuario is not None:
                        print("usuario =", usuario)
                        return render(request, 'usuarios/Eliminar.html', {"usuariof":usuario})
                    else:
                        return render(request, 'usuarios/Eliminar.html',{})
                except usuario.DoesNotExist:
                    messages.error(request,"ese usuario no existe")
                    return render(request, 'usuarios/Eliminar.html', {})
            else:
                return render(request, 'usuarios/Eliminar.html', {})
    else:
        return render(request, 'usuarios/Eliminar.html', {})

###################buscador de modificar
@login_required
def buscamod(request):
    if request.method == 'POST':
            buscaUsuario = request.POST['buscar']
            print(buscaUsuario)
            if buscaUsuario != "":
                try:
                    usuario = Usuario.objects.all()
                    usuario = Usuario.objects.filter(
                        Q(email = buscaUsuario)
                        ).distinct()
                    print(usuario)
                    if usuario is not None:
                        print("usuario =", usuario)
                        return render(request, 'usuarios/Modificar.html', {"usuario":usuario})
                    else:
                        return render(request, 'usuarios/Modificar.html',{})
                except usuario.DoesNotExist:
                    messages.error(request,"ese usuario no existe")
                    return render(request, 'usuarios/Modificar.html', {})
            else:
                return render(request, 'usuarios/Modificar.html', {})
    else:
        return render(request, 'usuarios/Modificar.html', {})

@login_required
def EliminaUsuario(request):
    if request.method == 'POST':
            vcorreo = request.POST['incorreo']
            print(vcorreo)
            print("hola")
            if vcorreo != "":
                try:
                    usuario = Usuario()
                    usuario= Usuario.objects.get(email=vcorreo)
                    print(usuario)
                    print("ahora se eliminara el usuario anterior")
                    if usuario is not None:
                        print("usuario =", usuario)
                        usuario.delete()
                        messages.success(request,"Usuario Eliminado")
                        return redirect(to=Listado)
                    else:
                        messages.error(request,"No se ha podido eliminar el usuario")
                        return render(request, 'usuarios/Eliminar.html',{})
                except usuario.DoesNotExist:
                    messages.error(request,"ese usuario no existe")
                    return render(request, 'usuarios/Eliminar.html', {})
            else:
                messages.error(request,"No se ha podido eliminar el usuario")
                return render(request, 'usuarios/Eliminar.html', {})
    else:
        messages.error(request,"No se ha podido eliminar el usuario")
        return render(request, 'usuarios/Eliminar.html', {})

@login_required
def modificarU(request):
    print("Agregando usuario")
    if request.method == 'POST':
        # sucursal = Sucursal()
        Vid = request.POST['id']
        Vnombre= request.POST['innombre']
        print(Vnombre)
        Vapellido= request.POST['inapellido']
        Vlink =  request.POST['inlink']
        Vrol= Rol.objects.get(id_rol =  request.POST['inrol'])
        print(Vrol)
        Vsucursal= Sucursal.objects.get(id_sucursal =  request.POST['insucursal'])
        print(Vsucursal)
        if Vid != "":
            try:
               print("try")
               usuario = Usuario.objects.get(id=Vid)
               usuario.username         = Vnombre
               usuario.last_name        = Vapellido
               usuario.link             = Vlink
               usuario.id_rol           = Vrol
               usuario.id_sucursal      = Vsucursal
               print(usuario)
               print("antes de guardar")
               usuario.save()
               print("guardado")
               print(usuario)
               messages.success(request,"usuario modificado correctamente")
               return redirect(to=Listado)
            except usuario.DoesNotExist:
               print("el error")
               messages.error(request,"ese usuario no existe")
               return render(request, 'usuarios/Modificar.html', {})
        else:
            messages.error(request,"No se ha podido modificar el usuario")
            return render(request, 'usuarios/Modificar.html', {})
    else:
        messages.error(request,"No se ha podido modificar el usuario")
        return render(request, 'usuarios/Modificar.html', {})

def Borrar(request, Uid):
    print('entre a mov',Uid)
    usuario= Usuario.objects.get(id=Uid)
    context = {"usuariof": usuario}
    print("termine")
    return render(request, 'usuarios/Eliminar.html', context)

def Editar(request, Uid):
    print('entre a mov',Uid)
    usuario= Usuario.objects.get(id=Uid)
    context = {"usuario": usuario}
    print("termine")
    return render(request, 'usuarios/Modificar.html', context)