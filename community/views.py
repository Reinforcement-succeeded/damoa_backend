from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from community.serializers import CommunitySerializer, UserAndCommunitySerializer

from community.models import Community as CommunityModel
from community.models import UserAndCommunity as UserAndCommunityModel
# Create your views here.
class MainLoginedCommunity(APIView):
    def get(self, request):
        user = request.user
        data = {}
        if user.is_anonymous:
            public_community = CommunityModel.objects.filter(is_public=True)
            serializer = CommunitySerializer(public_community, many=True)
            data['community'] = serializer.data
            data['tag'] = []
            for s_datas in serializer.data:
                for s_data in s_datas['tag']:
                    if s_data['name'] not in data['tag']:
                        data['tag'].append(s_data['name'])

            return Response(data, status=200)
        
        user_community = UserAndCommunityModel.objects.filter(user = request.user)
        user_community_serializer = UserAndCommunitySerializer(user_community, many=True)
        data['community'] = user_community_serializer.data
        data['tag'] = []
        for s_datas in user_community_serializer.data:
            for s_data in s_datas['community_info']['tag']:
                if s_data['name'] not in data['tag']:
                    data['tag'].append(s_data['name'])
                      
        return Response(data, status=200)