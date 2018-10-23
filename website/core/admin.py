from django.contrib import admin

# Register your models here.

from .models import User,Person,Pet,LostPet

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Pet)
admin.site.register(LostPet)