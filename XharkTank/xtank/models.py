from django.db import models

# Create your models here.

class Pitch(models.Model):
    entrepreneur = models.CharField(max_length=50)
    pitchTitle = models.CharField(max_length=100)
    pitchIdea = models.CharField(max_length=500)
    askAmount = models.FloatField( default=None, null=True)
    equity = models.FloatField( default=None, null=True)

    def __str__(self):
        return self.pitchTitle

class Offer(models.Model):
    pitch = models.ForeignKey(Pitch, default= None, null= True, related_name="offers", on_delete=models.CASCADE)
    investor = models.CharField(max_length=50)
    amount = models.FloatField(default= None, null=True)
    equity = models.FloatField(default= None, null=True)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.investor


