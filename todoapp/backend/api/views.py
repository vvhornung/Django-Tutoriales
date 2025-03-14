from rest_framework import generics, permissions
from .serializers import ToDoSerializer ,TodoToggleCompleteSerializer # Changed from TodoSerializer
from todo.models import ToDo  # Changed from Todo
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


class ToDoListCreate(generics.ListCreateAPIView): 
   
    serializer_class = ToDoSerializer  
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return ToDo.objects.filter(user=user).order_by('-created')  
        return ToDo.objects.none() 
        
    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
        

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer  
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
       
        return ToDo.objects.filter(user=user)  

class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)
    def perform_update(self,serializer):
        
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()
        
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) 
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. choose another username'},
                status=400)
   
    return JsonResponse({'error': 'POST request required'}, status=405)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'])
        if user is None:
            return JsonResponse(
                {'error': 'unable to login. check username and password'}, 
                status=400)
        else: 
            try:
                token = Token.objects.get(user=user)
            except: 
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
 
    return JsonResponse({'error': 'POST request required'}, status=405)