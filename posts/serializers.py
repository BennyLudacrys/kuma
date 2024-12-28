from cloudinary.utils import cloudinary_url
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post
from comments.serializers import CommentSerializer


class PersonSerializer(ModelSerializer):
    owner_first_name = serializers.CharField(source='owner.first_name', read_only=True)
    owner_last_name = serializers.CharField(source='owner.last_name', read_only=True)
    owner_picture = serializers.ImageField(source='owner.picture', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'created_at', 'updated_at', 'first_name', 'last_name', 'nationality', 'latitude', 'longitude',
                  'address', 'block', 'neighborhood', 'houseNumber', 'date_of_birth', 'date_of_disappearance',
                  'last_seen_location', 'cellphone', 'cellphone1', 'description', 'disease', 'picture', 'status',
                  'is_complete', 'owner_first_name', 'owner_last_name', 'kinship', 'province', 'gender', 'allergies',
                  'medical_conditions', 'medications', 'owner_picture', 'comments')

    # Função auxiliar para gerar a URL completa
    def get_picture_url(self, picture_name):
        # Gera o URL completo da imagem com o nome do arquivo
        if picture_name:
            picture_url, _ = cloudinary_url(f'photos/{picture_name}')
            return picture_url
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Se o post tem uma imagem, obtenha a URL completa usando o método get_picture_url
        if instance.picture:
            representation['picture'] = self.get_picture_url(instance.picture)

        # Se o proprietário tem uma imagem, obtenha a URL completa
        if instance.owner.picture:
            representation['owner_picture'] = self.get_picture_url(instance.owner.picture)

        return representation
