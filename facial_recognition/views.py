import cloudinary
import cloudinary.uploader
import urllib.request
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from django.http import JsonResponse
from posts.models import Post
from rest_framework.decorators import api_view
from io import BytesIO
import requests

# Função auxiliar para obter o URL correto da imagem
def get_picture_url(picture_name):
    if picture_name:
        picture_url, _ = cloudinary.utils.cloudinary_url(f'photos/{picture_name}')
        return picture_url
    return None

@api_view(['POST'])
def detect_image(request):
    # Configurações do Cloudinary diretamente na classe
    cloudinary.config(
        cloud_name='drxn8xsyi',
        api_key='785413883832964',
        api_secret='FOiok4tpbRm3obrJ56EintpBlG8'
    )

    # Verifica se uma imagem foi enviada na solicitação
    if request.method == 'POST' and request.FILES.get('image'):
        myfile = request.FILES['image']

        # Upload para o Cloudinary
        response = cloudinary.uploader.upload(myfile, folder='photos')
        uploaded_file_url = response['secure_url']

        # Inicializa listas para armazenar dados de rostos conhecidos
        images = []
        encodings = []
        names = []
        files = []
        person_data = []

        # Busca rostos conhecidos da database
        posts = Post.objects.all()
        for post in posts:
            images.append(post.first_name + '_image')
            encodings.append(post.first_name + '_face_encoding')
            files.append(get_picture_url(post.picture))  # Ajusta para obter a URL correta
            names.append(post.first_name + ' ' + post.address)

        # Carrega codificações e nomes dos rostos conhecidos
        known_face_encodings = []
        for i, image_path in enumerate(files):
            if image_path:
                response = requests.get(image_path)
                response.raise_for_status()
                image = face_recognition.load_image_file(BytesIO(response.content))
                encoding = face_recognition.face_encodings(image)
                if len(encoding) > 0:
                    known_face_encodings.append(encoding[0])

        known_face_names = names

        # Baixa a imagem desconhecida do Cloudinary
        response = requests.get(uploaded_file_url)
        response.raise_for_status()
        unknown_image = face_recognition.load_image_file(BytesIO(response.content))

        # Detecta rostos e codificações na imagem desconhecida
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        # Verifica se foram detectados rostos
        if len(face_encodings) == 0:
            return JsonResponse({'error': 'Nenhuma face detectada na imagem.'})

        # Converte a imagem para formato PIL
        pil_image = Image.fromarray(unknown_image)
        draw = ImageDraw.Draw(pil_image)

        # Loop através de cada face detectada
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Desconhecido"
            data = {}

            # Identifica a melhor correspondência
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = int(np.argmin(face_distances))
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                post = posts[best_match_index]

                # Extrai dados do Post correspondente
                data = {
                    'first_name': post.first_name,
                    'last_name': post.last_name,
                    'address': post.address,
                    'latitude': post.latitude,
                    'longitude': post.longitude,
                    'status': post.status,
                    'cellphone': post.cellphone,
                    'cellphone1': post.cellphone1,
                    'description': post.description,
                    'created_at': post.created_at,
                    'owner_picture': get_picture_url(post.picture),
                    'owner': get_picture_url(post.owner.picture),

                    'identified_by': request.user.username,
                    'owner_last_name': post.owner.last_name,



                    'owner_first_name': post.owner.first_name,
                    'detected_by_count': post.get_detected_by_count()



                }

                # Verifica se o usuário já detectou essa pessoa
                if request.user not in post.detected_by.all():
                    post.detected_by.add(request.user)
                    post.save()
                else:
                    data['error'] = 'Person already detected by this user.'

            # Desenha um retângulo ao redor do rosto
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
            draw.text((left, bottom), name, fill=(255, 255, 255, 255))

            # Adiciona os dados da pessoa à lista
            person_data.append(data)

        # Remove o objeto de desenho da memória
        del draw

        # Salva a imagem resultante no Cloudinary
        result_image = BytesIO()
        pil_image.save(result_image, format="JPEG")
        result_image_response = cloudinary.uploader.upload(result_image.getvalue(), resource_type="image", folder="results")
        result_image_url = result_image_response['secure_url']

        # Retorna os resultados como JSON
        return JsonResponse({'result_image_url': result_image_url, 'person_data': person_data})

    return JsonResponse({'error': 'Nenhuma imagem foi enviada.'})
