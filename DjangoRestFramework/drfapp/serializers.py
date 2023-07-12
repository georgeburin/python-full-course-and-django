#create serializers.py file in the app, not in main project

from rest_framework import serializers  #import serializers
from .models import Student 

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = (
      'name', 'age'   #when there is going to be a post request then we would expect 'name':'something' and same for 'age'. TEST THIS USING POSTMAN HTTP REQUEST POST. and create a post request with keys of name and age and pass any value you want with those keys
    )