from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateTimeField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        crea e restituisce una nuova istanza di article sulla base
        dei dati validati
        """
        print('Metodo Create del Serializer')
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        aggiorna e restituisce una istanza di article sulla base
        dei dati validati
        """
        print('Metodo Update del Serializer')
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title'
                                            , instance.title)

        instance.description = validated_data.get('description'
                                                  , instance.description)
        instance.body = validated_data.get('body'
                                           , instance.body)
        instance.location = validated_data.get('location'
                                               , instance.location)
        instance.publication_date = validated_data.get('publication_date'
                                                       , instance.publication_date)
        instance.active = validated_data.get('active'
                                             , instance.active)
        instance.save()
        return instance
