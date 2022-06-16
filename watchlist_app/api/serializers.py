
from rest_framework import serializers
from watchlist_app.models import *

class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source = 'platform.name')
    class Meta:
        model = WatchList
        fields = "__all__"
    # def create(self, validated_data):
    #     return WatchList.objects.create(**validated_data)

        
 
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields  = "__all__"        
        

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"        
        exclude = ('watchlist',)