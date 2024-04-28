from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Noise
from api.serializers.noise import NoiseSerializer


class NoiseView(APIView):
    def get(self, request):
        noises = Noise.objects.all()
        serializer = NoiseSerializer(noises, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NoiseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)