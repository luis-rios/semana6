from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='tag_de_publicacion')
    def publicacion(self, request, pk=None):
        tag = self.get_object()
        if request.method == 'GET':
            serializer = TagSerializer(tag.publicacion, many=True)
            return Response(status=status.HTTP_200_OK, data = serializer.data)

        if request.methos == 'POST':
            publicacion_id = request.data['publicacion_id']
            for publicaciones in publicacion_id:
                publicacion = Publicacion.objects.get(id=int(publicaciones))
                tag.publicacion.add(publicacion)
                return Response(status=status.HTTP_200_OK)
        if request.methos == 'DELETE':
            publicacion_id = request.data['publicacion_id']
            for publicaciones in publicacion_id:
                publicacion = Publicacion.objects.get(id=int(publicaciones))
                tag.publicacion.remove(publicacion)
                return Response(status=status.HTTP_200_OK)
