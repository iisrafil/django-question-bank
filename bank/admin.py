from django.contrib import admin
from bank.models import Category, SubCategory, Question


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Question)

