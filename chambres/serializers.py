from rest_framework import serializers
from .models import Concessionaire, Ville, Commune, Locale

class ConcessionnaireSerializer(serializers.ModelSerializer):
    # chbre_proche = LocaleSerializer(many=True)
    class Meta:
        model = Concessionaire
        fields = (
            'id',
            'libelle',
            'contacts',
            'email',
            'adresse',
            'site_internet',
        )

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = (
            'id',
            'libelle'
        )

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = (
            'id',
            'ville',
            'libelle',
        )
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['ville'] = VilleSerializer(instance.ville).data
        return response

class LocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locale
        fields = (
            'id',
            'commune',
            'concessionnaire',
            'chbre_proche',
            'libelle',
            'type_equipement',
            'profondeur_cable',
            'latitude',
            'longitude',
            'dtce_chambre_proche',
        )
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['concessionnaire'] = ConcessionnaireSerializer(instance.concessionnaire).data
        response['commune'] = CommuneSerializer(instance.commune).data
        response['chbre_proche'] = LocaleSerializer(instance.chbre_proche).data
        return response