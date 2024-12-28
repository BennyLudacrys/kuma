from cloudinary.utils import cloudinary_url
from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True
    )
    picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber', 'alternativePhoneNumber', 'password', 'last_name', 'first_name',
                  'country', 'province', 'address', 'picture', 'token')
        read_only_fields = ['token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    # Função auxiliar para gerar a URL completa
    def get_picture_url(self, picture_name):
        # Gera o URL completo da imagem com o nome do arquivo
        if picture_name:
            picture_url, _ = cloudinary_url(f'photos/{picture_name}')
            return picture_url
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Se o usuário tem uma imagem, obtenha a URL completa
        if instance.picture:
            representation['picture'] = self.get_picture_url(instance.picture)

        return representation


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'token')
        read_only_fields = ['token']


class UpdateUserSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True, required=False, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber', 'alternativePhoneNumber', 'password', 'last_name', 'first_name',
                  'country', 'province', 'address', 'picture', 'token')
        read_only_fields = ['token']

    def validate(self, attrs):
        if 'username' in attrs:
            if not User.objects.filter(username=attrs['username']).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError({'username': 'This username is already taken.'})

        if 'email' in attrs:
            if not User.objects.filter(email=attrs['email']).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError({'email': 'This email is already taken.'})

        if 'password' in attrs and len(attrs['password']) < 6:
            raise serializers.ValidationError({'password': 'Password must be at least 6 characters long.'})

        return attrs
