from django.contrib import admin
from .models import Products,Event
# Register your models here.
from .models import ContactMessage

admin.site.register(ContactMessage)
admin.site.register([Products,Event])