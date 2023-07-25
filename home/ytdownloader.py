import instaloader
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request
import requests
from django.http import HttpResponse
from django.core.files.base import ContentFile



@api_view()

def ytdownload(request):
    file_url = request.GET['link']  # Get the file URL from the query parameters

    if file_url:
        try:
            # Fetch the file from the URL

            
            return HttpResponse('File uploaded successfully.')

        except Exception as e:
            # Handle any errors that occur during the file upload
            return HttpResponse(f'Error uploading file: {str(e)}', status=500)

    else:
        return HttpResponse('File URL is missing.', status=400)
