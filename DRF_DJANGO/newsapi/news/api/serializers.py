from rest_framework import serializers
from news.models import Article, Journalist
from datetime import datetime
from django.utils.timesince import timesince


        
class ArticleSerializer(serializers.ModelSerializer):
    
    time_since_publicaton = serializers.SerializerMethodField()
    author_pk = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.StringRelatedField()
    #author = JournalistSerializer()
    
    class Meta:
        model = Article
        exclude = ('id',)
        
    def get_time_since_publicaton(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Titolo e descrizione non possono essere uguali')
        return data
    
    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError('Scrivi un titolo di almeno 60c')
        return value


class JournalistSerializer(serializers.ModelSerializer):
    #articles = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True,
                                     view_name='article_detail_apiview',
                                     read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"
        

'''
class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateTimeField()
    active = serializers.BooleanField()
    create_date = serializers.DateTimeField(read_only=True)
    update_date = serializers.DateTimeField(read_only=True)

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
    
    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError('Titolo e descrizione non possono essere uguali')
        return data
    
    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError('Scrivi un titolo di almeno 60c')
        return value
'''