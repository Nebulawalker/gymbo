from rest_framework import serializers


class ContentBlock:
    def __init__(self, id, title, video_url, impressions_quantity):
        self.id = id
        self.title = title
        self.video_url = video_url
        self.impressions_quantity = impressions_quantity


class ContentBlockSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    video_url = serializers.URLField(max_length=200)
    impressions_quantity = serializers.IntegerField()
