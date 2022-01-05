from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from testapp.serializers import NameSerializers
# Create your views here.
class TestViewSets(ViewSet):
    def list(self,request):
        colors=['green','red','blue','white']
        return Response({'msg':'Happy diwali','colors':colors})
    def create(self,request):
        serializer=NameSerializers(data=request.data)   #json data to python dict
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg=f'hello {name}, Happy New Year'
            return Response({'msg':msg})               #Response is use to convert python dict to json data
        else:
            return Response(serializer.errors,status=400)
    def update(self,request,pk=None):
        return Response({"msg":"this is from update"})
    def partial_update(self,request,pk=None):
        return Response({"msg":"this is from partial_update"})
    def retrieve(self,request,pk=None):
        return Response({"msg":"this is from retrieve"})
    def destroy(self,request,pk=None):
        return Response({"msg":"this is from destroy"})

class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors=['green','red','blue','white']
        return Response({'msg':'Happy Pongal','colors':colors})
    def post(self,request,*args,**kwargs):
        print(request.data,type(request.data))
        serializer=NameSerializers(data=request.data)   #json data to python dict
        if serializer.is_valid():
            name=serializer.data.get('name')
            msg=f'hello {name}, Happy Pongal'
            return Response({'msg':msg})               #Response is use to convert python dict to json data
        else:
            return Response(serializer.errors,status=400)
    def put(self,request,*args,**kwargs):
        return Response({'msg':'this from put'})

    def patch(self,request,*args,**kwargs):
        return Response({'msg':'this from patch'})

    def delete(self,request,*args,**kwargs):
        return Response({'msg':'this from delete'})
