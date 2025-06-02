from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from . import serializers, models
from rest_framework import generics

class CarDataListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        id_car_type = request.query_params.get('car_type_id')
        id_car_mark = request.query_params.get("mark_id")
        id_car_model = request.query_params.get("model_id")
        id_car_generation = request.query_params.get("generation_id")

        if id_car_type:
            car_mark_queryset = models.CarMark.objects.all()
            car_mark_serializer = serializers.CarMarkSerializer(car_mark_queryset, many=True)
            response = {
                "type_field": "mark_id",
                "data": car_mark_serializer.data,
            }
            if id_car_mark:
                car_model_queryset = models.CarModel.objects.filter(id_car_mark=id_car_mark).select_related(
                    "id_car_mark"
                )
                car_model_serializer = serializers.CarModelSerializer(car_model_queryset, many=True)
                response = {
                    "type_field": "model_id",
                    "data": car_model_serializer.data,
                }
                if id_car_model:
                    car_generation_queryset = models.CarGeneration.objects.filter(id_car_model=id_car_model).select_related(
                        "id_car_model"
                    )
                    car_generation_serializer = serializers.CarGenerationSerializer(car_generation_queryset, many=True)
                    response = {
                        "type_field": "generation_id",
                        "data": car_generation_serializer.data
                    }
                    if id_car_generation:
                        return Response({"message": "OK"})
            return Response(response)
        else:
            car_type_queryset = models.CarType.objects.all()
            car_type_serializer = serializers.CarTypeSerializer(car_type_queryset, many=True)
            response = {
                "type_field": "car_type_id",
                "data": car_type_serializer.data
            }
            return Response(response)


class PublicDataView(generics.GenericAPIView):
    def get(self, request):
        data = serializers.CombinedCarSerializer({
            "car_type": models.CarType.objects.only('id', 'name'),
            "fuel": models.Fuel.objects.only('id', 'name'),
            "transmission": models.Transmission.objects.only('id', 'name'),
            "gearbox_box": models.GearBox.objects.only('id', 'name'),
            "color": models.CarColor.objects.only('id', 'name'),
        }).data
        return Response(data, status=status.HTTP_200_OK)

class CarPostList(generics.ListAPIView):
    """Возврощает список автомобилей"""
    queryset = models.CarPost.objects.all()
    serializer_class = serializers.CarPostSerializer