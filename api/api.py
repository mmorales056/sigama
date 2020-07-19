from rest_framework import generics,permissions
from rest_framework.response import Response
from .serializers import ContactSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class= ContactSerializer

    def post(self,request,*args,**kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()
        return Response({
            "contact": ContactSerializer(contact,context=self.get_serializer_context()).data
        })

