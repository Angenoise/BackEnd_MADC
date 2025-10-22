# studentapi/serializers.py

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # These are the fields that will be converted to JSON
        fields = ['id', 'student_id', 'full_name', 'course', 'year_level']