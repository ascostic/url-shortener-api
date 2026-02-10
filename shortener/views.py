from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ShortURL
from .serializers import ShortURLSerializer


class CreateShortURLView(APIView):

    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RedirectShortURLView(APIView):

    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortURL, short_code=short_code)
        url_obj.click_count += 1
        url_obj.save()
        return HttpResponseRedirect(url_obj.original_url)
