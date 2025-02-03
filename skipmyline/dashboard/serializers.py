from rest_framework import serializers
from .models import Product, Shelf, ShelfAnalytics, SectionUsage, Segment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = '__all__'

class ShelfAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelfAnalytics
        fields = '__all__'

class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = '__all__'
        
class SectionUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionUsage
        fields = '__all__'
        
