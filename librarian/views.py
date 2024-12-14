from django.shortcuts import render
from Admin.serializers import LibrarianLoginSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from Admin.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

# login function for the librarian
class LibrarianLoginView(generics.GenericAPIView):
    serializer_class = LibrarianLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = LibrarianLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # fetch  the user by username
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
        
            # Create JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'full_name': user.username,
                'user_type': user.role,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        

