from django.contrib import admin
from field.models import *

# Register your models here.
# class FieldApplicationAdmin(admin.ModelAdmin):
# 	list_display=['firstname','middlename','lastname','regno','department','level',
# 	'course','year','allocation','phone_number','approved']

admin.site.register(FieldApplication)

admin.site.register(Profile)
