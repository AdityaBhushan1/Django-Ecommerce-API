# views.py

from django.urls import URLPattern, URLResolver
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.urls.resolvers import get_resolver


# views.py

def extract_urls(url_patterns, app_name, namespace=''):
    urls_list = []
    for pattern in url_patterns:
        if isinstance(pattern, URLPattern):
            name = f"{namespace}:{pattern.name}" if namespace else pattern.name
            path = pattern.pattern._route
            urls_list.append({'name': name, 'path': path})
        elif isinstance(pattern, URLResolver):
            namespace = f"{namespace}:{pattern.namespace}" if pattern.namespace else pattern.namespace
            urls_list.extend(extract_urls(pattern.url_patterns, app_name, namespace))
    return urls_list

@api_view(['GET'])
def app_urls(request, app_name):
    app_urls_list = []
    try:
        resolver = get_resolver(f'{app_name}.urls')
        app_urls_list = extract_urls(resolver.url_patterns, app_name)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {   
            'app_name':app_name,
            'app_urls':app_urls_list
        }, 
        status=status.HTTP_200_OK
        )
