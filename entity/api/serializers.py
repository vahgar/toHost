from rest_framework import serializers

from entity.models import business_entity

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = business_entity
        depth = 2
        fields = [
            'name',
            'profile',
            'services',
            'timings',
            'contact_person',
            'address',
            'mobile',
            'whatsapp',
            'Email',
            'website',
            'social_media',
            'city',
            'area',
            'locality',
            'category',
            'subcategory',
            'subsubcategory'
            ]
