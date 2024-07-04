from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
import re
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.cards.models import Card
from apps.cards.serializers import CardSerializer

class CardCreateAPIView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class CardUploadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['file'],
        properties={
            'file': openapi.Schema(type=openapi.TYPE_FILE, format=openapi.FORMAT_BINARY)
        }
    ))
    def post(self, request, format=None):
        if 'file' not in request.data:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        file_obj = request.FILES.get('file')
        if not hasattr(file_obj, 'name') or not file_obj.name:
            return Response(
                {"error": "Missing filename. Request should include a Content-Disposition header with a filename parameter."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        lines = file_obj.readlines()
        for line in lines:
            match = re.match(r'^[C\d]+\s+(\d+)', line.decode('utf-8'))
            if match:
                card_number = match.group(1)
                Card.objects.get_or_create(number=card_number)
        
        return Response(
            {"message": "Cards created successfully"},
            status=status.HTTP_201_CREATED)
    

class CardDetailAPIView(generics.RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'number'

class CardListAPIView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]