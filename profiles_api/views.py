from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    '''Test API View'''
    serializers_class = serializers.HelloSerializer
    def get(self, request, format=None):
        '''Returns a list APIView featurs'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application  logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'res': an_apiview})

    def post(self, request):
        '''Create a hello message with our name and email'''
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({'method' : 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    '''Test API ViewSet'''

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        '''Return a Hello Message'''

        a_viewset = [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionaltiy with less code',
        ]

        return Response({'message' : 'hello', 'a_viewset' : a_viewset})

    def create(self, request):
        '''Creates new hello message'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            message = f'hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''Handle getting an object'''
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        '''Handle updating an object'''
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        '''Hande partial update'''
        return Response({'htttp_method': 'PATCH'})

    def destroy(self, request, pk=None):
        '''Handle removing an object'''
        return Response({'http_method': 'DELETE'})
