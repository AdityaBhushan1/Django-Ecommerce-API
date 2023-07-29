from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

@api_view(['GET'])
def home(request):
    data = {
        'status':'200',
        'message':'Welcome To Murphy Threads Backend API!!!'
    }
    return Response(data)

# Specify an empty list for permission_classes to remove the default permissions
# home.permission_classes = []
home.permission_classes = [AllowAny]