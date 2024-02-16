from rest_framework.decorators import api_view
from user_app.api.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app.api import models

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=200)


# we are going to use function based view : so define function directly
@api_view(['POST'])
def register_user(request):
    data = {}
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registeration successfull"
            data['username'] = account.username
            data['email'] = account.email
            tokin = Token.objects.get(user=account)
            data['token'] = str(tokin)
        else:    
            data = serializer.error_messages    
                    
        return Response(data, status=201)