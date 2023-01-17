import datetime
from django import forms
from .models import recipe, dish, product,DishComposition, DailyReport


class DailyReportForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d.%m.%Y'], initial=datetime.date.today(), widget=forms.DateInput(format = '%d.%m.%Y', attrs={'placeholder': 'дд.мм.гггг', 'class': 'input_field'}))
    dish_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название блюда', 'class': 'input_field'}))
    count = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Количество проданных блюд', 'class': 'input_field'}))

    class Meta:
        model = DailyReport
        fields = ('date', 'dish_name', 'count')


class DishCompositionForm(forms.ModelForm):
    name = forms.CharField(label='Название продукта', widget=forms.TextInput(attrs={'placeholder': 'Название продукта', 'class': 'input_field'}))
    product_count = forms.IntegerField(label='Количество', widget=forms.TextInput(attrs={'placeholder': 'Количество', 'class': 'input_field'}))

    class Meta:
        model = DishComposition
        fields = ('name', 'product_count')


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Название продукта', widget=forms.TextInput(attrs={'placeholder': 'Название продукта', 'class': 'input_field'}))
    weight = forms.IntegerField(label='Вес продукта', widget=forms.TextInput(attrs={'placeholder': 'Вес продукта', 'class': 'input_field'}))
    calories = forms.IntegerField(label='Калорийность продукта', widget=forms.TextInput(attrs={'placeholder': 'Калорийность продукта', 'class': 'input_field'}))
    price = forms.DecimalField(label='Цена продукта', widget=forms.TextInput(attrs={'placeholder': 'Цена продукта', 'class': 'input_field'}))

    class Meta:
        model = product
        fields = ('name', 'weight', 'calories', 'price')


class RecipeForm(forms.ModelForm):
    name = forms.CharField(label='Название рецепта', widget=forms.TextInput(attrs={'placeholder': 'Название рецепта', 'class': 'input_field'}))
    cooking_time = forms.CharField(label='Время приготовления', widget=forms.TextInput(attrs={'placeholder': 'Время приготовления', 'class': 'input_field'}))
    cooking_technology = forms.CharField(label='Технология приготовления', widget=forms.Textarea(attrs={'placeholder': 'Технология приготовления', 'class': 'input_field_area'}))
    
    class Meta:
        model = recipe
        fields = ('name', 'cooking_time', 'cooking_technology')

class DishForm(forms.ModelForm):
    name = forms.CharField(label='Название блюда', widget=forms.TextInput(attrs={'placeholder': 'Название блюда', 'class': 'input_field'}))
    type = forms.CharField(label='Тип блюда', widget=forms.TextInput(attrs={'placeholder': 'Тип блюда', 'class': 'input_field'}))
    img = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'input_image', 'accept': 'image/', 'onchange': 'download(this)'}))

    class Meta:
        model = dish
        fields = ('name', 'type', 'img')
