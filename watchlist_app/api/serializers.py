from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    id = serializers.PrimaryKeyRelatedField(read_only=True)  
    
    def save(self):
        platform_name = self.validated_data['platform']['name']
        platform = StreamPlatform.objects.get(name=platform_name)
        watchlist = WatchList(
            title=self.validated_data['title'],
            description=self.validated_data['description'],
            platform = platform)
        watchlist.save()
        return watchlist
    
    def update(self, instance, validated_data):
        platform_name = validated_data['platform']
        validated_data['platform'] = StreamPlatform.objects.filter(name=platform_name)[0]
        return super().update(instance, validated_data)

    class Meta:
        model = WatchList
        fields = ['id', 'title', 'description', 'platform', 'avg_rating']
        fields = "__all__"
       


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"