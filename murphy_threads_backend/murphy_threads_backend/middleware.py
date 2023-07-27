# MIDDLEWARE.py
from django.http import HttpResponseForbidden
from django.conf import settings

class ApiKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to the home page without requiring an API key
        if request.path == '/':
            return self.get_response(request)

        # Check for the presence of the API key in the request headers
        api_key = request.headers.get('Api-Key')

        # Validate the API key
        if api_key == settings.API_KEY:
            return self.get_response(request)

        # Return permission error for other paths
        return HttpResponseForbidden('Permission Denied')
