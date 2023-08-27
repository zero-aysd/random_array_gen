from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
import logging
from rest_framework import serializers




logger = logging.getLogger(__name__)
# Create your views here.


class SentenceSerializer(serializers.Serializer):
    sentence = serializers.CharField()
    
class RandomArrayView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sentence = request.data.get("sentence")

        if not sentence:
            return Response({"error": "Missing 'sentence' parameter"}, status=status.HTTP_400_BAD_REQUEST)
        elif not isinstance(sentence, str):
            return Response({"error": "Invalid sentence value"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            random_array = self.generate_random_floats(0, 1, 500)
        except Exception as e:
            logger.error("An error occurred while generating random array: %s", str(e))
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        logger.info("Random array generated successfully.")
        return Response(random_array, status=status.HTTP_200_OK)

    def generate_random_floats(self, minimum:int,  maximum:int, lim:int):                  
        return [random.uniform(minimum, maximum) for _ in range(lim)]