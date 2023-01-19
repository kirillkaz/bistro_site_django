from main_app.error_messages import ERROR
from datetime import datetime
def CheckProduct(request):
    product_name_abc = 'йцукенгшщзхъфывапролджэячсмитьбюё '
    product_weight_calories_abc = '1234567890'
    product_price_abc = '1234567890.'

    error = ''
    try:
        prod_name = request.POST['name']
        prod_weight = request.POST['weight']
        prod_calories = request.POST['calories']
        prod_price = request.POST['price']

        for i in prod_name:
            if i not in product_name_abc:
                error = ERROR['INCORRECT_PRODUCT_NAME']
                return error
        
        for i in prod_weight:
            if i not in product_weight_calories_abc:
                error = ERROR['INCORRECT_PRODUCT_WEIGHT']
                return error

        for i in prod_calories:
            if i not in product_weight_calories_abc:
                error = ERROR['INCORRECT_PRODUCT_CALORIES']
                return error

        for i in prod_price:
            if i not in product_price_abc:
                error = ERROR['INCORRECT_PRODUCT_PRICE']
                return error

        if len(prod_name) < 2:
            error = ERROR['LITTLE_PRODUCT_NAME']
        elif len(prod_name) > 30:
            error = ERROR['BIG_PRODUCT_NAME']

        elif int(prod_weight) < 1:
            error = ERROR['LITTLE_PRODUCT_WEIGHT']
        elif int(prod_weight) > 1000:
            error = ERROR['BIG_PRODUCT_WEIGHT']

        elif int(prod_calories) < 30:
            error = ERROR['LITTLE_PRODUCT_CALORIES']
        elif int(prod_calories) > 10000:
            error = ERROR['BIG_PRODUCT_CALORIES']

        elif float(prod_price) < 10.00:
            error = ERROR['LITTLE_PRODUCT_PRICE']
        elif float(prod_price) > 5000.00:
            error = ERROR['BIG_PRODUCT_PRICE']
    except Exception as ex:
        error = f'Возникла внутренняя ошибка!'

    return error


def CheckRecipe(request):
    recipe_name_first_abc = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
    recipe_name_abc = 'йцукенгшщзхъфывапролджэячсмитьбюё '
    recipe_time_abc = '1234567890'
    recipe_technology_abc = 'йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ!"№;%:?*()_+"№;:?-=><,./\\ \'1234567890|'
    error = ''

    try:
        recipe_name = request.POST['name']
        recipe_time = request.POST['cooking_time']
        recipe_technology = request.POST['cooking_technology']

        for i in range(len(recipe_name)):
            if i == 0:
                if recipe_name[i] not in recipe_name_first_abc:
                    error = ERROR['INCORRECT_RECIPE_NAME']
                    return error
            elif recipe_name[i] not in recipe_name_abc:
                error = ERROR['INCORRECT_RECIPE_NAME']
                return error

        for i in recipe_time:
            if i not in recipe_time_abc:
                error = ERROR['INCORRECT_RECIPE_TIME']
                return error

        for i in recipe_technology:
            if i not in recipe_technology_abc:
                error = ERROR['INCORRECT_RECIPE_TECHNOLOGY']
                return error

        if len(recipe_name) < 2:
            error = ERROR['LITTLE_RECIPE_NAME']
        elif len(recipe_name) > 30:
            error = ERROR['BIG_RECIPE_NAME']
        elif int(recipe_time) < 5:
            error = ERROR['LITTLE_RECIPE_TIME']
        elif int(recipe_time) > 120:
            error = ERROR['BIG_RECIPE_TIME']
        elif len(recipe_technology) < 10:
            error = ERROR['LITTLE_RECIPE_TECHNOLOGY']
        elif len(recipe_technology) > 1000:
            error = ERROR['BIG_RECIPE_TECHNOLOGY']


    except Exception as ex:
        error = 'Возникла внутренняя ошибка!'

    return error


def CheckDish(request):
    error = ''
    #img_formats = ['img','jpg','jpeg','png']
    dish_type_abc = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    dish_type_firstletter_abc = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' 
    try:
        dish_type = request.POST['type']

        for i in range(len(dish_type)):
            if i == 0:
                if dish_type[0] not in dish_type_firstletter_abc:
                    error = ERROR['INCORRECT_DISH_TYPE']
                    return error
            else:
                if dish_type[i] not in dish_type_abc:
                    error = ERROR['INCORRECT_DISH_TYPE']
                    return error
    
        if len(dish_type) < 2:
            error = ERROR['LITTLE_DISH_TYPE']
        elif len(dish_type) > 10:
            error = ERROR['BIG_DISH_TYPE']

    except Exception as ex:
        error = 'Возникла внутренняя ошибка!'

    return error

def CheckDailyreport(request):
    error = ''
    date_abc = '1234567890.'
    count_abc = '1234567890'
    now = datetime.now()
    try:
        dailyreport_date = request.POST['date']
        dailyreport_count = request.POST['count']
        month_31_days = ['01','03','05','07','08','10','12']
        month_30_days = ['04','06','09','11']
        for i in dailyreport_date:
            if i not in date_abc:
                error = ERROR['INCORRECT_DATE_FORMAT']
                return error

        for i in dailyreport_count:
            if i not in count_abc:
                error = ERROR['INCORRECT_DAILYREPORT_COUNT']
                return error

        parced_date = dailyreport_date.split('.')
        
        if int(parced_date[1]) < 1 or int(parced_date[1]) > 12:
            error = ERROR['INCORRECT_DATE_FORMAT']
        elif int(dailyreport_count) < 1:
            error = ERROR['LITTLE_DAILYREPORT_COUNT']
        elif int(dailyreport_count) > 200:
            error = ERROR['BIG_DAILYREPORT_COUNT']
        elif int(parced_date[-1]) < 2020:
            error = ERROR['LITTLE_DAILYREPORT_DATE']
        elif int(parced_date[-1]) > now.year:
            error = ERROR['BIG_DAILYREPORT_DATE']
        elif int(parced_date[0]) < 1:
            error = ERROR['INCORRECT_DATE_FORMAT']
        elif parced_date[1] in month_31_days:
            if int(parced_date[0]) > 31:
                error = ERROR['INCORRECT_DATE_FORMAT']
        elif parced_date[1] in month_30_days:
            if int(parced_date[0]) > 30:
                error = ERROR['INCORRECT_DATE_FORMAT']
        elif parced_date[1] == '02':
            if int(parced_date[-1]) % 4 == 0:
                if int(parced_date[0]) > 29:
                    error = ERROR['INCORRECT_DATE_FORMAT']
            else:
                if int(parced_date[0]) > 28:
                    error = ERROR['INCORRECT_DATE_FORMAT']
    
    except Exception as ex:
        #error = ex
        error = 'Возникла внутренняя ошибка!'
    return error

def CheckDishcomposition(request):
    error = ''
    product_count_abc = '1234567890'
    try:
        product_count = request.POST['product_count']
        
        for i in product_count:
            if i not in product_count_abc:
                error = ERROR['INCORRECT_DISHCOMPOSITION_COUNT']
                return error
        
        if int(product_count) < 1:
            error = ERROR['LITTLE_DISHCOMPOSITION_COUNT']
        elif int(product_count) > 100:
            error = ERROR['BIG_DISHCOMPOSITION_COUNT']
    except Exception as ex:
        error = 'Возникла внутренняя ошибка!'

    return error
