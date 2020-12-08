from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer


class PublicacionViewSets(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='publicacion_usuario')
    def publicar(self, request, pk=None):
        publicacion = self.get_object()
        if request.method == 'GET':
            serializer = PublicacionSerializer(publicacion.comentario)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        if request.method == 'POST':
            comentario_id = request.data['comentario_id']
            for comentarios in comentario_id:
                comentario = Comentario.objects.get(id=int(comentario_id))
                publicacion.comentario.add(comentario)
                return Response(status=status.HTTP_200_OK)
        if request.method == 'DELETE':
            comentario_id = request.data['comentario_id']
            for comentarios in comentario_id:
                comentario = Comentario.objects.get(id=int(comentario_id))
                publicacion.comentario.remove(comentario)
                return Response(status=status.HTTP_200_OK)