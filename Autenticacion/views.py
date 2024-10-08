from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages

class Registro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'registro/Registro.html', {'form':form})
    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'registro/Registro.html', {'form':form})
def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')
            usuario = authenticate(username=nombre, password=clave)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                messages.error(request, 'Credenciales incorrectas')
        else:
            messages.error(request, 'Credenciales incorrectas')
    else:
        form=AuthenticationForm()
    return render(request, 'login/Login.html', {'form':form})