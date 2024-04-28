from django.contrib.gis.measure import Distance
from geopy.distance import distance
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Noise


from django.contrib.gis.measure import Distance


class NoiseSingleView(APIView):
    def get(self, request):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')

        if latitude is None or longitude is None:
            return Response({"error": "Latitude and longitude are required."}, status=400)

        user_location = (float(latitude), float(longitude))

        noise_data = Noise.objects.all()

        closest_noises = []
        num_closest = 5
        search_radius = Distance(m=200)
        while not closest_noises:
            closest_noises = []
            for noise_entry in noise_data:
                noise_location = (noise_entry.latitude, noise_entry.longitude)
                dist = distance(user_location, noise_location).meters
                if dist <= search_radius.m:
                    closest_noises.append(noise_entry)
            search_radius += Distance(m=200)

        total_decibels = sum(noise.decibels for noise in closest_noises)
        average_decibels = total_decibels / len(closest_noises) if closest_noises else 0

        response_data = {
            "average_decibels": average_decibels,
            "search_radius": search_radius.m
        }

        return Response(response_data)

