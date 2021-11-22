from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, get_user_model, logout

from .forms import LoginForm
from .serializers import LocaleSerializer
from .models import Locale, Concessionaire, Ville, Commune


def connexion(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            dj_login(request, user)
            group = request.user.groups.filter(user=request.user)[0]
            if group.name == "ADMIN":
                messages.success(request, "Bienvenue : {}".format(username))
                return HttpResponseRedirect(reverse('chambres:dashboard'))
            else:
                messages.error(request, "Désolé vous n'estes pas encore enregistrer dans notre Sytème")
                return HttpResponseRedirect(reverse('connexion'))
        else:
            request.session['invalid_user'] = 1 # 1 == True
            messages.error(request, "Echec de Connexion, Assurez-vous d'avoir entrer le bon login et le bon Mot de Passe SVP !")
            return HttpResponseRedirect(reverse('connexion'))
    return render(request, 'login.html', {'login_form': login_form})

def loggout(request):
    logout(request)
    return HttpResponseRedirect(reverse('chambres:connexion'))

def dashboard(request):
    chambres = Locale.objects.all().order_by('libelle')
    nb_chambres = chambres.count()
    nb_concessionnaires = Concessionaire.objects.all().count()
    nb_ville = Ville.objects.all().count()
    nb_commune = Commune.objects.all().count()
    context = {
        'chambres': chambres,
        'nb_chambres': nb_chambres,
        'nb_concessionnaires': nb_concessionnaires,
        'nb_ville': nb_ville,
        'nb_commune': nb_commune,
    }
    return render(request, 'chambres/dashboad.html', context)

@api_view(['GET'])
def chambres(request):
    chambres = Locale.objects.all().order_by('libelle')
    serializer = LocaleSerializer(chambres, many=True)
    return Response(serializer.data)

def localisation(request):
    chambres = Locale.objects.all()
    chambres_count = chambres.count()
    context = {
        'chambres' : chambres,
        'chambres_count':chambres_count,
        # 'parcelle_count':parcelle_count
    }
    return render(request, 'carte.html', context)

# Create your views here.
