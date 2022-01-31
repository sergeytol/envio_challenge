from os import getenv

from dateutil.parser import parse
from django.db.models import Avg
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ReadingListSerializer, ReadingAggrInputSerializer
from .models import Reading


class ReadingCreateApi(CreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingListSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"success": True}, status=status.HTTP_201_CREATED)


class ReadingAggrApi(APIView):

    def get(self, request):

        serializer = ReadingAggrInputSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        filters = {
            'aggr_size_min':
                self.request.query_params.get('aggr_size_min')
                or getenv('AGGR_SIZE_MINUTES_DEFAULT', 5),
            'device_id': self.request.query_params.get('device_id'),
            'customer_id': self.request.query_params.get('customer_id'),
            'from': self.request.query_params.get('from'),
            'to': self.request.query_params.get('to'),
        }

        filters['aggr_size_min'] = int(filters['aggr_size_min'])
        filters['from'] = parse(filters['from']).isoformat() if filters['from'] else None
        filters['to'] = parse(filters['to']).isoformat() if filters['to'] else None

        queryset = (
            Reading.timescale
                .time_bucket('time', f'{filters["aggr_size_min"]} minutes')
                .annotate(Avg('reading'))
                .values('device_id', 'customer_id', 'bucket', 'reading__avg')
                .order_by('device_id', 'bucket')
        )

        if filters['device_id']:
            queryset = queryset.filter(device_id=filters['device_id'])
        if filters['customer_id']:
            queryset = queryset.filter(customer_id=filters['customer_id'])
        if filters['from']:
            queryset = queryset.filter(time__gte=filters['from'])
        if filters['to']:
            queryset = queryset.filter(time__lte=filters['to'])

        devices_list = []
        devices_list_index = 0

        def next_round(index):
            devices_list.append({
                'device_id': queryset[index]['device_id'],
                'customer_id': queryset[index]['customer_id'],
                'from': filters['from'],
                'to': filters['to'],
                'aggregation_size_minutes': filters['aggr_size_min'],
                'aggregated_values': []
            })

        for index in range(len(queryset)):
            if index == 0:
                next_round(index)
            devices_list[devices_list_index]['aggregated_values'].append({
                'from': queryset[index]['bucket'].isoformat(),
                'value': queryset[index]['reading__avg']
            })
            if index < len(queryset) - 1:
                if queryset[index]['device_id'] != queryset[index+1]['device_id']:
                    next_round(index+1)
                    devices_list_index += 1

        return Response({"data": devices_list})
