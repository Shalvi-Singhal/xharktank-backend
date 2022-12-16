from rest_framework import serializers
from xtank.models import Pitch, Offer


class OfferSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    class Meta:
      model = Offer
      fields = ('id','pitch','investor', 'amount', 'equity', 'comment')

      

class PitchSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    offers = OfferSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Pitch.objects.create(**validated_data)

    class Meta:
        model = Pitch
        fields = ('id', 'entrepreneur', 'pitchTitle', 'pitchIdea', 'askAmount', 'equity', 'offers')
        
 




