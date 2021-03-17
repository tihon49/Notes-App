from rest_framework import serializers
from app.models import Note, Product


class ProductSerializer(serializers.ModelSerializer):
    """продукт"""
    value = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'value', 'count', 'completed']


class NotesListSerializer(serializers.ModelSerializer):
    """отображение всех заметок"""
    products = ProductSerializer(many=True, read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = ['id', 'name', 'products', 'completed', 'owner']


class NoteDetailSerializer(serializers.ModelSerializer):
    """детальное отображение заметки"""
    products = ProductSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = '__all__' # ['id', 'name', 'products']
