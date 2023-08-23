from rest_framework import serializers
from .models import Film, Actor, Category, Info


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class FilmSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    actor_name = serializers.SerializerMethodField()

    def get_actor_name(self, obj):
        info = Info.objects.filter(film_id= obj.id)
        result = []
        for pen in info:
            exemple = {"id": pen.actor.id, "first_name": pen.actor.first_name}
            result.append(exemple)
        return result
    class Meta:
        model = Film
        fields = "__all__"




