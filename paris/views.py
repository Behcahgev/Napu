from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .models import Profile
# Create your views here.

#EXAMPLES
def home(request):
    return HttpResponse(
        "<h1>Test</h1>"
    )


def equipe(request,id_equipe):

    if id_equipe > 100:
        #return redirect(home)
        #return redirect(equipe,id_equipe=42) #nom de la fonction vue
        #return redirect('mon_equipe',id_equipe=42) #nom de l'url
        raise Http404

    return HttpResponse(
        "equipe: {0}".format(id_equipe)
    )

def date_actuelle(request):
    date = datetime.now()
    nombre1 = 5
    nombre2 = 6
    couleurs = {
        'FF0000':'rouge',
        'ED7F10':'orange',
        'FFFF00':'jaune',
        '00FF00':'vert',
        '0000FF':'bleu',
        '4B0082':'indigo',
        '660099':'violet',
    }
    #return render(request, 'paris/date.html',{'date': datetime.now()})
    return render(request,'paris/date.html',locals()) #envoie les données locales à la fonction


#END EXAMPLES


def connexion(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect(hub)
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = LoginForm()

    return render(request, 'paris/login.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(connexion)

#homePage
@login_required
def hub(request):

    return render(request,'paris/home.html',locals())


    
