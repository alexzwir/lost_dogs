from django.db import models

# How to use a photo in this case?
# And when user have more that one pet?
# How to set an age, when you have the birthday?

class User(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Person(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    personal_photo = models.CharField(max_length=50)
    personal_pet = models.CharField(max_length=50)

class Pet(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_age = models.CharField(max_length=50)
    pet_birthday = models.CharField(max_length=50)
    pet_type = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    pet_chip_number = models.CharField(max_length=50)
    pet_lost = models.BooleanField(max_length=50)
    
class LostPet(models.Model):
    lost_pet_pointing = models.CharField(max_length=50)