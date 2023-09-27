from django.http import JsonResponse
from django.shortcuts import render
from dj_rest_auth.views import LoginView as DefaultLoginView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, OperationLevelSerializer
from .models import User, OperationLevel
# Create your views here.

# class UserDetailsView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#     # Get the "Authorization" header from the request
#         authorization_header = request.META.get('HTTP_AUTHORIZATION', '')

#         # Extract the token from the header (assuming it's in the "Bearer" format)
#         token = authorization_header.split('Bearer ')[1].strip() if authorization_header.startswith('Bearer ') else None

#         # Now, you can print the token or use it as needed
#         print("Token received:", token)

#         serializer = self.get_serializer(request.user)
#         print(serializer.data)
#         print(type(request.user))
#         return JsonResponse(serializer.data)

    
#     def get_object(self):
#         print("ENTRA AQUI")
#         return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve the current authenticated user using self.request.user
        return User.objects.filter(id=self.request.user.id)
    
    # def update(self, request, *args, **kwargs):
    #     # update operation_level 
    #     operation_level = request.data.get('operation_level')
    #     user = User.objects.get(id=self.request.user.id)
    #     user.operation_level = operation_level
    #     user.save()
    #     return super().update(request, *args, **kwargs)
    
class OperationLevelViewSet(viewsets.ModelViewSet):
    serializer_class = OperationLevelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return OperationLevel.objects.filter(id=self.request.user.id)
        # return OperationLevel.objects.all()
        return OperationLevel.objects.filter(user=self.request.user)

    

