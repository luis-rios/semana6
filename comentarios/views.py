from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='comentario_usuario')
    def comentario(self, request, pk=None):
        publicacion = self.get_object()

        if request.method == 'GET':
            serializer = ComentarioSerializer(publicacion.comentario)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            comentario_id = request.data['comentario_id']
            for comentarios in comentario_id:
                comentario = Publicacion.objects.get(id=int(comentarios))
                publicacion.comentario.add(comentario)
                return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            comentario_id = request.data['comentario_id']
            for comentarios in comentario_id:
                comentario = Publicacion.objects.get(id=int(comentarios))
                publicacion.comentario.remove(comentario)
                return Response(status=status.HTTP_200_OK)


