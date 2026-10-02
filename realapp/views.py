from .models import MyUser1
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import User1Serializer
# Create your views here.

@api_view(['GET'])
def get_user_profile_data(request, pk):
    
    try:
        try:
            user = MyUser1.objects.get(username=pk)
        except MyUser1.DoesNotExist:
            return Response({'error':'user does not exist'})

        serializer = User1Serializer(user, many=False)
        return Response(serializer.data)
    except:
        return Response({'error':'error getting user data'})
    

 