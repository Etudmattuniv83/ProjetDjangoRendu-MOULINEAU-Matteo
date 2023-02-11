from rest_framework import serializers
from .models import Annonce
class AnnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annonce
        fields = ('id','titre','categorie','prix','description','date_debut','vendeur_nom','vendeur_telephone','vendeur_ville')
