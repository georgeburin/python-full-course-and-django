from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 

#now do authentication:
#from rest_framework.permissions import AllowAny
#above line is for everyone to use our api
from rest_framework.permissions import IsAuthenticated 


from drfapp.serializers import StudentSerializer
from drfapp.models import Student 

class TesView(APIView):
  # def get(self, request, *args, **kwargs):    #get request
  #   data = {   #this is dictionary - data structure, not JSON - data format
  #     'username': 'admin',
  #     'years_active': 10
  #   }
  #   return Response(data)   THIS WOULD JUST RETURN data DICTIONARY THAT WE JUST CREATED above to any get request 

  permission_classes = (IsAuthenticated, )
  #NOW if you want to use this external api. for example you make a GET request you can no longer get 
  #the data without providing 'Authorization':'Token 7811978f5ca8bb88ceb6d907e6a9133eae8c2f72'
  #inside the header

  def get(self, request, *args, **kwargs):
    qs = Student.objects.all() #get all objects from the Student database
    serializer = StudentSerializer(qs, many=True) #since more than 1 object we have to specify many=True

    #we can also do the following
    #student1=qs.first()
    #serializer = StudentSerializer(student1)
    #then we do our responce as below but we return only the first user from the database
    return Response(serializer.data) #return JSON data
  
  def post(self, request, *args, **kwargs):
    serializer = StudentSerializer(data=request.data)  #(data=request.data) because we want to get the data from the user. ITs a post request  
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      Response(serializer.error)



