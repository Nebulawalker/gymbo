from .models import Page, Impression
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContentBlockSerializer, ContentBlock


class PagesAPIView(APIView):
    def get(self, request):
        result = []
        pages = Page.objects.all()
        for page in pages:
            page_url = request.build_absolute_uri(page.get_absolute_url())
            content_blocks = page.content_blocks.values_list('title', flat=True)
            result.append({
                'page_url': page_url,
                'content_blocks': content_blocks
            })
        return Response(result)


class PageDetailView(APIView):
    def get(self, request, slug):
        page = Page.objects.get(slug=slug)
        content_blocks = [block for block in page.content_blocks.all()]
        result = []
        for content_block in content_blocks:
            impressions, is_created = Impression.objects.get_or_create(
                page=page,
                content_block=content_block
            )
            impressions.quantity += 1
            impressions.save()
            result.append(
                ContentBlock(
                    content_block.id,
                    content_block.title,
                    content_block.video_url,
                    content_block.impression.filter(
                        page=page
                    ).values_list('quantity', flat=True)[0])
            )
        return Response(ContentBlockSerializer(result, many=True).data)
