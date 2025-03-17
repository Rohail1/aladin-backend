from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response


USER = get_user_model()


@api_view(['POST'])
def signup(request):
    try:
        pass
    except:
        return Response({'Error', 'ok'})

@api_view(['POST'])
def login(request):
    return Response({})

