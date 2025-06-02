from rest_framework import serializers
from . import models

class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarType
        fields = "__all__"

class CarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarMark
        fields = "__all__"

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarModel
        fields = "__all__"

class CarGenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarGeneration
        fields = "__all__"

class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fuel
        fields = "__all__"

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transmission
        fields = "__all__"

class GearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GearBox
        fields = "__all__"

class CarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarColor
        fields = "__all__"

class CombinedCarSerializer(serializers.Serializer):
    car_type = CarTypeSerializer(many=True)
    fuel = FuelSerializer(many=True)
    transmission = TransmissionSerializer(many=True)
    gearbox_box = GearBoxSerializer(many=True)
    color = CarColorSerializer(many=True)

class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarPost
        fields = '__all__'