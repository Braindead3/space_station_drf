from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import Station, Instructions
from .serializers import StationSerializer, InstructionsSerializer


class StationViewSet(viewsets.ModelViewSet):
    """
        Эндпоинты для космической станции.

        GET: предоставляет все станции
        POST: добовляет новую станцию
        PUT: обновляет информацию о станции полностью
        PATCH: частично обновляет информацию о станции

        GET: /stations/{station_id}/state/ - Получение координат станции.
        POST: /stations/{station_id}/state/ - Изменение позиции станции.
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer

    @extend_schema(
        request=InstructionsSerializer,
        responses={'200': inline_serializer('coordinates', {
            'x': serializers.IntegerField(),
            'y': serializers.IntegerField(),
            'z': serializers.IntegerField()
        })},
        methods=['GET', 'POST']
    )
    @action(methods=('GET', 'POST'), detail=True)
    def state(self, request, pk):
        if request.method == 'POST':
            ins_ser = InstructionsSerializer(data=request.data)

            if ins_ser.is_valid(raise_exception=True):
                ins_ser.save()

        station: Station = Station.objects.get(pk=pk)
        return Response(data={
            'x': station.x,
            'y': station.y,
            'z': station.z,
        }, status=status.HTTP_200_OK)
