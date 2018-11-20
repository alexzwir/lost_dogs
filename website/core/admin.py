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
        "person_updated_at",
    ]

    readonly_fields=["person_created_at","person_updated_at"]

    class Meta:
        model = Person

admin.site.register(CrewLostDog)
admin.site.register(User)
admin.site.register(Person,PersonModelAdmin)
admin.site.register(Pet)
admin.site.register(LostPet)
