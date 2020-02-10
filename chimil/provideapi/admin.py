from django.contrib import admin
from .models import Employee,Location
# Register your models here.
# registering Employee and Location models
admin.site.register(Employee)
admin.site.register(Location)