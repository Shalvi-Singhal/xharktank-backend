from rest_framework.response import Response
from rest_framework import status
from xtank.models import Pitch,Offer
from xtank.api.serializers import PitchSerializer, OfferSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
            
@api_view(['GET', 'POST'])
def pitch_list(request):
    if request.method == 'GET':
        pitches=Pitch.objects.all()
        serializer=PitchSerializer(pitches, many=True )
        return Response(serializer.data, status=200)

    if request.method == 'POST':
         #request.data['offers']={}
         serializer = PitchSerializer(data=request.data)
         if serializer.is_valid():   
             serializer.save()
             ID={'id' : str(serializer.data.get("id"))}
             return Response(ID, status=201)
         else:
             return Response(status=400)

@api_view()
def pitch_detail(request, pk):
    try:
        pitches=Pitch.objects.get(pk=pk)
        serializer=PitchSerializer(pitches)
        return Response(serializer.data, status=200)
    except:
        return Response(status=404)

@api_view(['POST'])
def counteroffer(request, pk):
    try:
        if request.method == 'POST':
            serializer = OfferSerializer(data=request.data)
            if serializer.is_valid():  
               obj=serializer.save()    
               #obj.pitch=int(pk)         
               ID={"id" : str(serializer.data.get("id"))}
       
               return Response(ID, status=201)
        else:
            return Response(status=400)
    except:
        return Response(status=404)
    
    


   