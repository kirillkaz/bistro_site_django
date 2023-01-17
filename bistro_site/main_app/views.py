from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, F
from main_app.forms import ProductForm, RecipeForm, DishForm, DishCompositionForm, DailyReportForm
from main_app.models import product, recipe, dish, DishComposition, DailyReport


@csrf_exempt
def LoadMakeFinallyReportPage(request):
    daily_reports = DailyReport.objects.raw(
            """
            select main_app_dailyreport.id as id,
            main_app_recipe.name as name,
            main_app_dailyreport.count,
            to_char(main_app_dailyreport."date",'DD.MM.YYYY') as date, 
            round(sum((main_app_product.price/1000.00)*main_app_product.weight*main_app_dishcomposition.product_count*main_app_dailyreport.count),2) as price
            from main_app_dailyreport
            inner join main_app_dishcomposition on main_app_dishcomposition.dish_id = main_app_dailyreport.dish_id 
            inner join main_app_product on main_app_product.id = main_app_dishcomposition.product_id
            inner join main_app_recipe on main_app_dishcomposition.dish_id = main_app_recipe.id
            where main_app_dailyreport.dish_id = main_app_dishcomposition.dish_id
            group by main_app_dailyreport."date", main_app_dailyreport.id, main_app_recipe.name, main_app_dailyreport.count
            order by date;
            """
            )

    finally_sums = DailyReport.objects.raw(
            """
            select 1 as id, extract(year from main_app_dailyreport."date") as date,  round(sum((main_app_product.price/1000.00)*main_app_product.weight*main_app_dishcomposition.product_count*main_app_dailyreport.count),2) as price
            from main_app_dailyreport
            inner join main_app_dishcomposition on main_app_dishcomposition.dish_id = main_app_dailyreport.dish_id 
            inner join main_app_product on main_app_product.id = main_app_dishcomposition.product_id
            inner join main_app_dish on main_app_dishcomposition.dish_id = main_app_dish.id_id
            where main_app_dailyreport.dish_id = main_app_dishcomposition.dish_id
            group by extract(year from main_app_dailyreport."date"), 1
            order by date
            """
            )
    
    daily_reports_results = DailyReport.objects.raw(
            """
            select 1 as id, to_char(main_app_dailyreport."date",'DD.MM.YYYY') as date,  round(sum((main_app_product.price/1000.00)*main_app_product.weight*main_app_dishcomposition.product_count*main_app_dailyreport.count),2) as price
            from main_app_dailyreport
            inner join main_app_dishcomposition on main_app_dishcomposition.dish_id = main_app_dailyreport.dish_id
            inner join main_app_product on main_app_product.id = main_app_dishcomposition.product_id
            inner join main_app_dish on main_app_dishcomposition.dish_id = main_app_dish.id_id
            where main_app_dailyreport.dish_id = main_app_dishcomposition.dish_id
            group by main_app_dailyreport."date", 1
            order by date
            """
            )

    cur_year = None
    cur_year_results = None
    days_results = []
    try:
        cur_year = request.GET['year']
    except:
        pass
    #выбираю текущий год
    for i in finally_sums:
        if cur_year == str(i.date):
            cur_year_results = i
            break
    #заполняю массив с продажами, актуальными на этот год
    for i in daily_reports:
        if i.date.split('.')[2] == cur_year:
            days_results.append(i)
    
    daily_reports_with_dishprices = []

    #записываю в массив записи о продажах + стоимость за одно блюдо
    for i in days_results:
        record = {'record': i, 'dish_price': round(i.price/i.count, 2)}
        daily_reports_with_dishprices.append(record)

    message = f'{days_results[0].date} {daily_reports_with_dishprices[0]["record"].date}'
    context = {'days_results': days_results, 'cur_year_results': cur_year_results, 'daily_reports_with_dishprices': daily_reports_with_dishprices, 'cur_year': cur_year, 'message': message}
    return render(request, 'main_app/FinallyReportPath/look_finallyreport.html', context)



@csrf_exempt
def LoadLookFinallyReportYearsPage(request):
    reports = DailyReport.objects.all().order_by('date')

    years = []

    for i in reports:
        year = i.date.year
        if year not in years:
            years.append(year)

    context = {'years': years}
    return render(request, 'main_app/FinallyReportPath/look_years_finallyreport.html', context)



@csrf_exempt
def LoadEditDailyReportPage(request):
    error = ''
    cur_name = None
    cur_date = None
    cur_id = None
    try:
        cur_name = request.GET['name']
        cur_date = request.GET['date']
        cur_id = request.GET['reportID']
    except:
        pass

    if request.method == 'POST':
        form = DailyReportForm(request.POST)
        if form.is_valid():
                
            if cur_name == None:
                error = f'Невозможно добавить информацию о продажах, так как блюда с названием {cur_name} не существует.'
            elif cur_date == None:
                error = f'Невозможно редактировать информацию о продажах, нет продажи этого блюда за {cur_date} число.'
            elif cur_id == None:
                error = f'Невозможно редактировать информации об этой продаже, так как ее не существует.'
            else:
                editable_dailyreport = DailyReport.objects.get(id=cur_id)
                editable_dailyreport.date = editable_dailyreport.date
                editable_dailyreport.count = form.cleaned_data.get('count')
                editable_dailyreport.save()
                return redirect('look_global_dailyreport')
        else:
            error = f'{form.cleaned_data.get("date")} {form.cleaned_data.get("dish_name")} {form.cleaned_data.get("count")}'

    form = DailyReportForm
    context={'form': form, 'error': error, 'cur_name': cur_name, 'cur_date': cur_date}

    return render(request, 'main_app/DailyReportPath/edit_dailyreport.html', context)



@csrf_exempt
def LoadLookLocalDailyReportPage(request):
    cur_date = ''
    try:
        cur_date = request.GET['date']
    except:
        pass
    # TODO потом разобраться и сделать нормально
    local_reports = DailyReport.objects.raw(
            """
            select main_app_dailyreport.id as id,
            main_app_recipe.name as name,
            main_app_dailyreport.count,
            to_char(main_app_dailyreport."date",'DD.MM.YYYY') as date, 
            round(sum((main_app_product.price/1000.00)*main_app_product.weight*main_app_dishcomposition.product_count*main_app_dailyreport.count),2) as price
            from main_app_dailyreport
            inner join main_app_dishcomposition on main_app_dishcomposition.dish_id = main_app_dailyreport.dish_id 
            inner join main_app_product on main_app_product.id = main_app_dishcomposition.product_id
            inner join main_app_recipe on main_app_dishcomposition.dish_id = main_app_recipe.id
            where main_app_dailyreport.dish_id = main_app_dishcomposition.dish_id
            group by main_app_dailyreport."date", main_app_dailyreport.id, main_app_recipe.name, main_app_dailyreport.count
            order by price;
            """
            )
    
    context = {'local_reports': local_reports, 'cur_date': cur_date}
    return render(request, 'main_app/DailyReportPath/look_dailyreport_local.html', context)


@csrf_exempt
def LoadLookGlobalDailyReportPage(request):
    # TODO потом разобраться и сделать нормально
    global_reports = DailyReport.objects.raw(
            """
            select 1 as id, to_char(main_app_dailyreport."date",'DD.MM.YYYY') as date,  round(sum((main_app_product.price/1000.00)*main_app_product.weight*main_app_dishcomposition.product_count*main_app_dailyreport.count),2) as price
            from main_app_dailyreport
            inner join main_app_dishcomposition on main_app_dishcomposition.dish_id = main_app_dailyreport.dish_id 
            inner join main_app_product on main_app_product.id = main_app_dishcomposition.product_id
            inner join main_app_dish on main_app_dishcomposition.dish_id = main_app_dish.id_id
            where main_app_dailyreport.dish_id = main_app_dishcomposition.dish_id
            group by main_app_dailyreport."date", 1
            order by date
            """
            )

    context = {'global_reports': global_reports}
    return render(request, 'main_app/DailyReportPath/look_dailyreport_global.html', context)


@csrf_exempt
def LoadAddDailyReportPage(request):
    error = ''
    if request.method == 'POST':
        form = DailyReportForm(request.POST)
        if form.is_valid():
            new_id = 1
        
            dailyreports = DailyReport.objects.all()
            dailyreports_id = [i.id for i in dailyreports]
            for i in range(1,1001):
                if i not in dailyreports_id:
                    new_id = i
                    break
                
            dish_name = form.cleaned_data.get('dish_name')
            enabled_recipe = None
            enabled_dish = None
            try:
                enabled_recipe = recipe.objects.get(name=dish_name)
                enabled_dish = dish.objects.get(id=enabled_recipe.id)
            except:
                pass

            if enabled_recipe == None or enabled_dish == None:
                error=f'Невозможно добавить информацию о продажах, так как блюда с названием {dish_name} не существует.'
            else:
                new_dailyreport = DailyReport()
                new_dailyreport.id = new_id
                new_dailyreport.date = form.cleaned_data.get('date')
                new_dailyreport.dish = enabled_dish
                new_dailyreport.count = form.cleaned_data.get('count')
                new_dailyreport.save()
        else:
            error = f'{form.cleaned_data.get("date")} {form.cleaned_data.get("dish_name")} {form.cleaned_data.get("count")}'
    form = DailyReportForm
    context={'form': form, 'error': error}

    return render(request, 'main_app/DailyReportPath/add_dailyreport.html', context)

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
    # TODO потом разобраться и сделать нормально
    dishes = dish.objects.raw(
            """
            select main_app_dish.id_id, main_app_dish."type", main_app_dish.img, sum(main_app_product.weight) as weight, sum(main_app_product.calories) as calories
            from main_app_product
            inner join main_app_dishcomposition on main_app_dishcomposition.product_id = main_app_product.id
            inner join main_app_dish on main_app_dish.id_id = main_app_dishcomposition.dish_id
            where main_app_dish.id_id = main_app_dishcomposition.dish_id
            group by main_app_dish.id_id, main_app_dish."type", main_app_dish.img order by id_id
            """
            )

    #dishes = dish.objects.all().order_by('id_id')
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

