from .models import Page, ContentBlock
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContentBlockSerializer


class PagesAPIView(APIView):
    def get(self, request):
        content_blocks = ContentBlock.objects.all()
        result = []
        for content_block in content_blocks:
            pages = [
                request.build_absolute_uri(
                    slug.get_absolute_url()
                ) for slug in Page.objects.filter(
                                  content_blocks=content_block
                              )
            ]
            result.append({
                'content_block_title': content_block.title,
                'page_urls': pages
            })
        return Response(result)


class PageDetailView(APIView):
    def get(self, request, slug):
        page = Page.objects.get(slug=slug)
        content_blocks = [block for block in page.content_blocks.all()]
        for content_block in content_blocks:
            content_block.views += 1
            content_block.save()
        return Response(ContentBlockSerializer(content_blocks, many=True).data)
