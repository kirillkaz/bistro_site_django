from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from main_app.forms import ProductForm, RecipeForm, DishForm, DishCompositionForm
from main_app.models import product, recipe, dish, DishComposition


@csrf_exempt
def LoadEditDishcompositionPage(request):
    error = ''
    dishcompositionID: int = 0

    try:
        dishcompositionID = request.GET['dishcompositionID']
    except:
        pass
    
    edited_dishcomposition = DishComposition.objects.get(record_id=dishcompositionID)

    if request.method == 'POST':
        form = DishCompositionForm(request.POST)
        form.name = 'Какое-то название'
        if form.is_valid():
            edited_dishcomposition.product_count = form.cleaned_data.get('product_count')
            edited_dishcomposition.save()
            return redirect(f'http://146.185.240.26/hub/look/dishcomposition?dishID={edited_dishcomposition.dish.id_id}')
        else:
            error = f'{form.cleaned_data.get("name")} {form.cleaned_data.get("product_count")}'
    
    product_name = product.objects.get(id=request.GET['productID']).name
    form = DishCompositionForm(initial={'name': edited_dishcomposition.dish.id.name, 'product_count': edited_dishcomposition.product_count})
    context={'form': form, 'error': error, 'cur_dish': edited_dishcomposition.dish, 'product_name': product_name}

    return render(request, 'main_app/DishCompositionPath/edit_dishcomposition.html', context)



@csrf_exempt
def LoadAddDishcompositionPage(request):
    error = ''
    if request.method == 'POST':
        form = DishCompositionForm(request.POST)
        if form.is_valid():
            new_id = 1
    
            dishcompositions = DishComposition.objects.all()
            dishcompositions_id = [i.record_id for i in dishcompositions]
            for i in range(1,1001):
                if i not in dishcompositions_id:
                    new_id = i
                    break

            product_name = form.cleaned_data.get('name')
            added_product = None
            editable_dish = dish.objects.get(id=request.GET['dishID'])

            try:
                added_product = product.objects.get(name=product_name)
            except:
                pass

            if added_product == None:
                error='Невозможно добавить продукт в состав, так как его нет на складе.'
            else:
                new_dishcomposition = DishComposition()
                new_dishcomposition.record_id = new_id
                new_dishcomposition.product_count = form.cleaned_data.get('product_count')
                new_dishcomposition.dish = editable_dish
                new_dishcomposition.product = added_product
                new_dishcomposition.save()
        else:
            error = f'{form.cleaned_data.get("name")} {form.cleaned_data.get("count")}'
    form = DishCompositionForm
    context={'form': form, 'error': error}

    return render(request, 'main_app/DishCompositionPath/add_dishcomposition.html', context)



@csrf_exempt
def LoadLookDishcompositionPage(request):
    if request.POST:
        if request.POST.get('button_type') == 'удалить':
            dishcomposition_product = DishComposition.objects.get(record_id = request.POST.get('record_id'))
            dishcomposition_product.delete()
            return redirect('look_dish')
    
    cur_dish = None
    try:
        cur_dish = dish.objects.get(id=request.GET['dishID'])
    except:
        pass
    dish_composition = DishComposition.objects.all().order_by('product_id')
    context = {'cur_dish': cur_dish, 'dish_composition': dish_composition}
    return render(request, 'main_app/DishCompositionPath/look_dishcomposition.html', context)



@csrf_exempt
def LoadEditDishPage(request):
    error = ''
    dishID: int = 1

    try:
        dishID = request.GET.get('dishID')
    except:
        pass
        
    editable_dish = dish.objects.get(id=dishID)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        form.name = 'Какое-то название'
        if form.is_valid():
            if request.POST.get('button_type') == 'Удалить':
                editable_dish.delete()
                return redirect('look_dish')
            else:
                editable_dish.img = form.cleaned_data.get('img')
                editable_dish.type = form.cleaned_data.get('type')
                editable_dish.save()
                return redirect('look_dish')
        else:
            error = f'{form.cleaned_data.get("type")} {form.cleaned_data.get("img")}'

    
    form = DishForm(initial={'name': editable_dish.id.name,'type': editable_dish.type, 'img': editable_dish.img})
    context = {'form': form, 'error': error, 'editable_dish': editable_dish}
    return render(request, 'main_app/DishPath/edit_dish.html', context)



@csrf_exempt
def LoadLookDishPage(request):
    dishes = dish.objects.all().order_by('id_id')
    dish_composition = DishComposition.objects.all()
    context = {'dishes': dishes, 'dish_composition': dish_composition}
    return render(request, 'main_app/DishPath/look_dish.html', context)


@csrf_exempt
def LoadAddDishPage(request):
    error = ''
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish_name = form.cleaned_data.get('name')
            dish_recipe = None

            try:
                dish_recipe = recipe.objects.get(name=dish_name)
            except:
                pass

            if dish_recipe == None:
                error='Невозможно создать блюдо, так как для него нет рецепта.'
            else:
                new_dish = dish()
                new_dish.id = dish_recipe
                new_dish.img = form.cleaned_data.get('img')
                new_dish.type = form.cleaned_data.get('type')
                new_dish.save()
        else:
            error = f'{form.cleaned_data.get("name")} {form.cleaned_data.get("img")}: {type(form.img)} {form.cleaned_data.get("type")} {request.FILES} {request.POST["img"]}'

    form = DishForm
    context={'form': form, 'error': error}

    return render(request, 'main_app/DishPath/add_dish.html', context)



@csrf_exempt
def LoadEditRecipePage(request):
    error = ''
    recipeID: int = 1

    try:
        recipeID = request.GET.get('recipeID')
    except:
        pass

    editable_recipe = recipe.objects.get(id=recipeID)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            if request.POST.get('button_type') == 'Удалить':
                editable_recipe.delete()
                return redirect('look_recipe')
            else:
                editable_recipe.name = form.cleaned_data.get('name')
                editable_recipe.cooking_time = form.cleaned_data.get('cooking_time')
                editable_recipe.cooking_technology = form.cleaned_data.get('cooking_technology')
                editable_recipe.save()
                return redirect('look_recipe')
        else:
            error = f'{form.cleaned_data.get("name")}\n{form.cleaned_data.get("cooking_time")}\n{form.cleaned_data.get("cooking_technology")}'


    form = RecipeForm(initial={'name': editable_recipe.name, 'cooking_time': editable_recipe.cooking_time, 'cooking_technology': editable_recipe.cooking_technology})
    context = {'form': form, 'error': error}
    return render(request, 'main_app/RecipePath/edit_recipe.html', context)



@csrf_exempt
def LoadLookRecipePage(request):
    recipes = recipe.objects.all().order_by('id')
    context = {'recipes': recipes}
    return render(request, 'main_app/RecipePath/look_recipes.html', context)


@csrf_exempt
def LoadAddRecipePage(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        new_id = 1
        
        recipes = recipe.objects.all()
        recipes_id = [i.id for i in recipes]
        for i in range(1,1001):
            if i not in recipes_id:
                new_id = i
                break
            
        if form.is_valid():
            new_recipe = recipe()
            new_recipe.id = new_id
            new_recipe.name = form.cleaned_data.get('name')
            new_recipe.cooking_time = form.cleaned_data.get('cooking_time')
            new_recipe.cooking_technology = form.cleaned_data.get('cooking_technology')
            new_recipe.save()
        else:
            error = f'{form.cleaned_data.get("name")}\n{form.cleaned_data.get("cooking_time")}\n{form.cleaned_data.get("cooking_technology")}'

    form = RecipeForm
    context={'form': form, 'error': error}

    return render(request, 'main_app/RecipePath/add_recipe.html', context)


@csrf_exempt
def LoadEditProdPage(request):
    error = ''
    prodID: int = 1
    
    try:
        prodID = request.GET.get('prodID')
    except:
        pass

    prod = product.objects.get(id=prodID)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            if request.POST.get('button_type') == 'Удалить':
                prod.delete()
                return redirect('look_prod')
            else:
                prod.name = form.cleaned_data.get('name')
                prod.weight = form.cleaned_data.get('weight')
                prod.calories = form.cleaned_data.get('calories')
                prod.price = form.cleaned_data.get('price')
                prod.save()
                return redirect('look_prod')
        else:
            error = f'{form.cleaned_data.get("name")}\n{form.cleaned_data.get("weight")}\n{form.cleaned_data.get("calories")}\n{form.cleaned_data.get("price")}'

    
    form = ProductForm(initial={'name': prod.name, 'weight': prod.weight, 'calories': prod.calories, 'price': prod.price})
    context = {'form': form, 'error': error}
    return render(request, 'main_app/ProductsPath/edit_product.html', context) 


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
    return render(request, 'main_app/ProductsPath/add_product.html', context)


def LoadLookProdPage(request):
    products = product.objects.all().order_by('id')
    context = {'products': products}
    return render(request, 'main_app/ProductsPath/look_products.html', context)


def LoadMainPage(request):
    context={}
    return render(request, 'main_app/main_page.html', context)

# Create your views here.

