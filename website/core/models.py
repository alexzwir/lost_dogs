from django.db import models
from django.utils import timezone
from django.utils.timesince import timesince

# How to use a photo in this case?
# And when user have more that one pet?
# How to set an age, when you have the birthday?

# def upload_image(instance,filename):
#     return "images/{user}/{filename}".format(user=instance.user,filename=filename)

class CrewLostDog(models.Model):
    crew_name = models.CharField(max_length=50)
    # crew_avatar_photo = models.ImageField(upload_to=upload_image,blank=True,null=True)
    crew_avatar_photo = models.ImageField(upload_to="website/core/uploads/",blank=True,null=True)
    crew_phone = models.CharField(max_length=50)
    crew_email = models.CharField(max_length=50)

    def __str__(self):
        return self.crew_name

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_avatar_photo = models.ImageField(blank=True,null=True)
    user_phone = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)

class Person(models.Model):
    person_name = models.CharField(max_length=50)
    person_phone = models.CharField(max_length=50)
    person_email = models.CharField(max_length=50)
    person_birthday = models.CharField(max_length=50)
    person_personal_photo = models.CharField(max_length=50)
    person_personal_pet = models.CharField(max_length=50)
    person_created_at = models.DateTimeField(auto_now_add=True,null=True)
    person_updated_at = models.DateTimeField(auto_now=True)

class Pet(models.Model):
    pet_name        = models.CharField(max_length=50)
    pet_age         = models.CharField(null=True)
    pet_birthday    = models.DateField(null=True)
    pet_type        = models.CharField(max_length=50)
    pet_breed       = models.CharField(max_length=50)
    pet_chip_number = models.CharField(max_length=50)
    pet_lost_flag   = models.BooleanField(max_length=50)
    pet_timestamp   = models.DateTimeField(auto_now_add=True,null=True)
    pet_updated_at  = models.DateTimeField(auto_now=True,null=True)

    def age(self):
        return(timesince(self.pet_age))
    
class LostPet(models.Model):
    lost_pet_pointing = models.CharField(max_length=50)
    lost_pet_photo = models.ImageField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lost_pet_pointing
    