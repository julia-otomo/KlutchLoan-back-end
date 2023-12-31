import imghdr
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Card
from .serializers import CardSerializer
from clients.models import Client
from django.shortcuts import get_object_or_404
import cloudinary.uploader


class ClientCardListCreateView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "cpf"

    def get_queryset(self):
        get_client_cpf = self.kwargs.get("cpf")
        queryset = super().get_queryset()
        client = get_object_or_404(Client, cpf=get_client_cpf)

        client_cards = queryset.filter(client=client)

        return client_cards

    def perform_create(self, serializer):
        get_client_cpf = self.kwargs.get("cpf")

        client = get_object_or_404(Client, cpf=get_client_cpf)

        front_image = self.request.data.get("front_image")
        back_image = self.request.data.get("back_image")
        selfie_image = self.request.data.get("selfie_image")

        allowed_image_mime_types = ["jpeg", "png", "gif", "jpg"]

        if not (front_image and back_image and selfie_image):
            raise ValidationError("Todos os campos de imagem são necessários.")

        def is_valid_image(file):
            image_format = imghdr.what(file)
            return image_format in allowed_image_mime_types

        for image in [front_image, back_image, selfie_image]:
            if not is_valid_image(image.file):
                raise ValidationError("Arquivos não compatíveis")

        front_image_cloud = cloudinary.uploader.upload(front_image)
        back_image_cloud = cloudinary.uploader.upload(back_image)
        selfie_image_cloud = cloudinary.uploader.upload(selfie_image)

        base_cloudinary_url = "http://res.cloudinary.com/dojrawoma/image/upload/"

        front_image_url = (
            base_cloudinary_url
            + front_image_cloud["public_id"]
            + "."
            + front_image_cloud["format"]
        )
        back_image_url = (
            base_cloudinary_url
            + back_image_cloud["public_id"]
            + "."
            + back_image_cloud["format"]
        )
        selfie_image_url = (
            base_cloudinary_url
            + selfie_image_cloud["public_id"]
            + "."
            + selfie_image_cloud["format"]
        )

        serializer.save(
            client=client,
            front_image=front_image_url,
            back_image=back_image_url,
            selfie_image=selfie_image_url,
        )

        return super().perform_create(serializer)


class CardDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    lookup_field = "card_number"
