from rest_framework import serializers
from .models import Addr


class AddrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addr
        fields = ["longaddr", "shortaddr", "date"]
