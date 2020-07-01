from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination

from account.api.serializers import BaseAccountSerializer, BaseAccount, UserProfileSerializer, UserProfile


@api_view(['POST'])
@permission_classes([AllowAny & ~IsAuthenticated])
def registration_view(request):
    serializer = BaseAccountSerializer(data=request.data)

    data = {}

    if serializer.is_valid():
        account = serializer.save()

        data['response'] = 'User registered successfully!'
        data['username'] = account.username
        data['email'] = account.email
        data['token'] = Token.objects.get(user=account).key
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = BaseAccount.objects.all()
    serializer_class = BaseAccountSerializer
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination
    

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    
    profile = None
    try:
        profile = UserProfile.objects.get(base__username=request.user.username)
    except UserProfile.DoesNotExist:
        return Response({'response': 'Not Found!'}, status=status.HTTP_404_NOT_FOUND)

    
    if request.method == 'GET':
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if (request.method == 'PUT'):
        serializer = UserProfileSerializer(profile, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class Profile(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

