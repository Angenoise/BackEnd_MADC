# studentapi/admin.py

from django.contrib import admin
from .models import Student # 1. Import your Student model

# 2. Register your model with the admin site
admin.site.register(Student)