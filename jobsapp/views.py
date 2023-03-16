from django.shortcuts import render
import jobsapp
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .paginator import Mypagination
from .serializers import *
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
import json
import base64
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
class Jobs(generics.ListCreateAPIView):
    pagination_class=Mypagination
    serializer_class=JobsSerialiser
    
    queryset=WebCompanyJobs.objects.all().order_by('posted_date')
    filter_backends = [filters.SearchFilter]
    search_fields = ['^job_title', '^company_name',]
    # filter_fields = {'job_title':['startswith'], 'company_name':['startswith'],'web_company_jobs_id':['exact']}
class getjob(APIView):
   def get(self,request):
       print("here in ")
       if self.request.GET.get('jobid'):
         try:
           data=WebCompanyJobs.objects.get(web_company_jobs_id=self.request.GET.get('jobid'))
           serializer=JobsSerialiser(data)
           return Response(serializer.data)
         except:
           return Response("eneter correct jobid")
       elif self.request.GET.get('job_title'): 
         print ("title")
         try:
           data=WebCompanyJobs.objects.filter(Q(job_title__icontains=self.request.GET.get('job_title'))|Q(company_name__icontains=request.GET.get('job_title')))
           print(data)
           serializer=JobsSerialiser(data,many=True)
           return Response(serializer.data)
         except:
           return Response(serializer)
         
       else:
        return Response("enter correct jobid")
      
      
class LoginORlogout(APIView):
      def get(self,request):
            if self.request.GET.get('login'):
            
              uname=base64.b64decode(self.request.GET.get('username')).decode("utf-8")
              pwd=base64.b64decode(self.request.GET.get('password')).decode("utf-8")
              print(uname,pwd)
              check_user=authenticate(username=uname, password=pwd)
              if check_user:
                 print('login sucessfull')
                 return Response({'status':'login sucessfull'})
              else:
                 return Response({'status':'login failed'})
            elif self.request.GET.get('logout')!=None:
                 logout(self.request)
                 return Response({'status':'logout sucessfull'})
      
      def post(self,request):
          data=json.loads(self.request.body)
          if User.objects.filter(username=data.get('username')).count()>0:
              return Response('user already exists')
          else:
              user = User(username=data.get('username'), password=data.get('password'))
              user.save()
              return Response({'status':'signup sucessfull'})    
                 
            
# def logindec(func):
#       def wrapper(*args, **kwargs):
#            if request.user.is_authenticated!=True
#                  return render(request,'jobsapp/list jobs.html')
#                   func()
#         return wrapper
              
                 
def renderjobs(request):
    return render(request,'jobsapp/list jobs.html')
def renderjob(request):
    return render(request,'jobsapp/showjob.html')
def login(request):
  return render(request,'jobsapp/login.html')