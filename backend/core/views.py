from django.shortcuts import render

from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ContactSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response


class ContactAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """
    serializer_class = ContactSerializer

    def get_serializer_context(self):
        """
        Permite a configuração do contexto do serializador,
        como o próprio request (onde é acessado os dados de envio e chamada),
        o formato (JSON nesse caso), e o objeto da classe
        """
        
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)
