from django.contrib import admin
from .models import Class, Join, Stream
# Register your models here.
admin.site.register([Class, Join, Stream])
