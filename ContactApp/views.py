from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    contact_form=ContactForm()
    if request.method=='POST':
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('nombre')
            email=request.POST.get('email')
            content=request.POST.get('contenido')
            email=EmailMessage('Mensaje desde App Django',
                               'El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n{}'.format(name,email,content),
                               '', ['mmsaant@gmail.com'],reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                #habria q gestionar bien la excepcion pero paso de ser pegiguera
                return redirect('/contacto/?invalido')
    return render(request,'contacto/Contacto.html',{'contact_form':contact_form})