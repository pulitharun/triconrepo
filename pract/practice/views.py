from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserDetails
from rest_framework import status 


class userview(APIView):
    def get(self, request,id=None):
        if id:
            result = UserDetails.objects.get(id=id)
            serializer = userserializer(result)
        else:
            result = UserDetails.objects.all()
            serializer = userserializer(result,many=True)
        return Response({'status': 'succes', 'user': serializer.data})
                
    def post(self, request):
        serializer = userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registered successfully!", 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'user not registered', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id=None):
        user = UserDetails.objects.filter(id=id)
        user.delete()
        return Response({'status' : 'success'})
    
    def put(self, request, id=None):
        user = UserDetails.objects.get(id=id)
        serializer = userserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully', 'data': serializer.data})
        return Response({'message': 'Failed to update user', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id=None):
        user = UserDetails.objects.get(id=id)
        serializer = userserializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User patched successfully', 'data': serializer.data})
        return Response({'message': 'Failed to patch user', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)