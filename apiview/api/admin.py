from django.contrib import admin
from .models import Data
# Register your models here.
@admin.register(Data)
class Inform(admin.ModelAdmin):
    list_display = ['id','name','roll','city']
