from django import forms
from .models import recipe, dish, product, DishComposition, DailyReport


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Название продукта', widget=forms.TextInput(attrs={'placeholder': 'Название продукта', 'class': 'input_field'}))
    weight = forms.IntegerField(label='Вес продукта', widget=forms.TextInput(attrs={'placeholder': 'Вес продукта', 'class': 'input_field'}))
    calories = forms.IntegerField(label='Калорийность продукта', widget=forms.TextInput(attrs={'placeholder': 'Калорийность продукта', 'class': 'input_field'}))
    price = forms.DecimalField(label='Цена продукта', widget=forms.TextInput(attrs={'placeholder': 'Цена продукта', 'class': 'input_field'}))

    class Meta:
        model = product
        fields = ('name', 'weight', 'calories', 'price')

class DishForm(forms.ModelForm):
    id = forms.IntegerField(label='Номер блюда')
    type = forms.CharField(label='Тип блюда')
    img = forms.ImageField(label='Картинка')

    class Meta:
        model = dish
        fields = ('id', 'type', 'img')
