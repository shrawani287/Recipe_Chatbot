from django.contrib import admin
from recipe.models import Contact1
from recipe.models import Food_data
# Register your models here.
from import_export.admin import ImportExportModelAdmin
admin.site.register(Contact1)
admin.site.register(Food_data)
