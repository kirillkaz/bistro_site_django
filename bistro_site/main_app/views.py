from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main_app.forms import ProductForm
from main_app.models import product

@csrf_exempt
def LoadAddProdPage(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        new_id = 1

        products = product.objects.all()
        prods_id = [i.id for i in products]
        for i in range(1,1001):
            if i not in prods_id:
                new_id = i
                break

        if form.is_valid():
            prod = product()
            prod.id=new_id
            prod.name=form.cleaned_data.get('name')
            prod.weight=form.cleaned_data.get('weight')
            prod.calories=form.cleaned_data.get('calories')
            prod.price=form.cleaned_data.get('price')
            prod.save()
        else:
            error = f'{form.cleaned_data.get("name")}\n{form.cleaned_data.get("weight")}\n{form.cleaned_data.get("calories")}\n{form.cleaned_data.get("price")}'

    form = ProductForm
    context={'form': form, 'error': error}
    return render(request, 'main_app/add_product.html', context)


def LoadLookProdPage(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, 'main_app/look_products.html', context)


def LoadMainPage(request):
    context={}
    return render(request, 'main_app/main_page.html', context)

# Create your views here.
