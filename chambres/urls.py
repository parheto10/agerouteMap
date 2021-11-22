from django.urls import path
from .views import chambres, loggout, connexion, dashboard, localisation

app_name='chambres'


urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('deconnexion/', loggout, name="deconnexion"),
    path('deconnexion/', loggout, name="deconnexion"),
    path('api/v1/chambres/', chambres, name="localisation"),
    path('carte/', localisation, name="localisation"),
    path('', connexion, name="connexion"),
]