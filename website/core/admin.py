from django.contrib import admin

# Register your models here.

from .models import User,Person,Pet,LostPet,CrewLostDog

class PersonModelAdmin(admin.ModelAdmin):
    fields = [
        "person_name",
        "person_phone",
        "person_email",
        "person_birthday",
        "person_personal_photo",
        "person_personal_pet",
        "person_created_at",
        "person_updated_at"
    ]

    readonly_fields=["person_created_at","person_updated_at"]

    class Meta:
        model = Person


class PetModelAdmin(admin.ModelAdmin):
    fields= [
        'pet_name',
        'pet_birthday',
        'pet_age',
        'get_age',
        'pet_type',
        'pet_chip_number',
        'pet_lost_flag',
        'pet_timestamp',
        'pet_updated_at'
    ]
    readonly_fields = ['get_age','pet_timestamp','pet_updated_at']

    def get_age(self,obj,*args, **kwargs):
        return str(obj.age)
    get_age.short_description = "Idade do Pet"

    class Meta:
        model = Pet



admin.site.register(CrewLostDog)
admin.site.register(User)
admin.site.register(Person,PersonModelAdmin)
admin.site.register(Pet,PetModelAdmin)
admin.site.register(LostPet)
