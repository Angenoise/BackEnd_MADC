# studentapi/views.py

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    # This one line of code does a lot! It tells the view:
    # 1. What data to work with (all Student objects).
    queryset = Student.objects.all()
    # 2. How to serialize that data (using the StudentSerializer we just made).
    serializer_class = StudentSerializer