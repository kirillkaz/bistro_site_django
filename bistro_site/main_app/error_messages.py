#product name
little_product_name = 'Ошибка! Минимальная длина названия продукта питания от 2 символов!'
big_product_name = 'Ошибка! Максимальная длина названия продукта питания не должна превышать 30 символов!'
incorrect_product_name = 'Ошибка! Название продуктов питания может состоять только из русских символов в нижнем регистре!'
#product_weight
little_product_weight = 'Ошибка! Минимальный вес продукта питания от 1 грамма!'
big_product_weight = 'Ошибка! Максимальный вес продукта питания не должен превышать 1 000 грамм!'
incorrect_product_weight = 'Ошибка! Вес продукта питания представляет из себя целое число от 1 до 100 000!'
#product_calories
little_product_calories = 'Ошибка! Минимальная калорийность продукта питания от 30Ккал!'
big_product_calories = 'Ошибка! Максимальная калорийность продукта питания не должна превышать 10 000Ккал!'
incorrect_product_calories = 'Ошибка! Калорийность продукта питанияпредставляет из себя целое число от 30 до 10 000!'
#product_price
little_product_price = 'Ошибка! Минимальная цена продукта питания от 10.00р!'
big_product_price = 'Ошибка! Максимальная цена продукта питания не должна превышать 5000.00р'
incorrect_product_price = 'Ошибка! Цена продукта представляет из себя вещественное число от 10.00 до 5000.00. Разделителем между целой и дробной частью - "."!'

#recipe_name
little_recipe_name = 'Ошибка! Минимальная длина названия рецепта блюда от 2 символов!'
big_recipe_name = 'Ошибка! Максимальная длина названия рецепта блюда не должна превышать 30 символов!'
incorrect_recipe_name = 'Ошибка! Название рецепта блюда состоит только из русских символов. Певрое слово должно начинаться с большой буквы, а остальные с маленькой!'
#recipe_time
little_recipe_time = 'Ошибка! Минимальное время приготовления блюда - 5 минут!'
big_recipe_time = 'Ошибка! Максимальное время приготовления блюда - 120 минут!'
incorrect_recipe_time = 'Ошибка! Время приготовления состоит только из целых чисел!'
#recipe_technology
little_recipe_technology = 'Ошибка! Минимальная длина технологии приготовления блюда от 10 символов!'
big_recipe_technology = 'Ошибка! Максимальная длина технологии приготовления блюда не должна превышать 1000 символов!'
incorrect_recipe_technology = 'Ошибка! Технология приготовления блюда состоит из русских символов в верхнем и нижнем регистре, цифр, а также из специальных символов!'

#dish_name - обработан в recipe_name
#dish_img
incorrect_img_format = 'Ошибка! Выбранный файл не является картинкой!'
#dish_type
little_dish_type = 'Ошибка! Минимальная длина вида блюда от 2 символов!'
big_dish_type = 'Ошибка! Максимальная длина вида блюда не должна превышать 10 символов!'
incorrect_dish_type = 'Ошибка! Вид блюда состоит только из русских букв. Первая буква должна быть заглавной!'

#daily_report_date
incorrect_date_format = 'Ошибка! Вы ввели некоректный формат даты. Корректный формат - дд.мм.гггг'
little_dailyreport_date = 'Ошибка! Вы не можете добавить продажу раньше 2020 года!'
big_dailyreport_date = 'Ошибка! Вы не можете добавить продажу позднее текущего года!'
#daily_report_count
little_dailyreport_count = 'Ошибка! Минимальное количиство проданных блюд от 1!'
big_dailyreport_count = 'Ошибка! Максимальное количество проданных блюд не может превышать 200!'
incorrect_dailyreport_count = 'Ошибка! Количество проданных блюд состоит только из целого числа!'

#dishcomposition_count
little_dishcomposition_count = 'Ошибка! Количество продуктов в составе блюда от 1!'
big_dishcomposition_count = 'Ошибка! Количество продуктов в составе блюда не должно превышать 100!'
incorrect_dishcomposition_count = 'Ошибка! Количество продуктов в составе блюда представляет из себя целое число!'
ERROR = {
    'LITTLE_PRODUCT_NAME': little_product_name,
    'BIG_PRODUCT_NAME': big_product_name,
    'INCORRECT_PRODUCT_NAME': incorrect_product_name,
    'LITTLE_PRODUCT_WEIGHT': little_product_weight,
    'BIG_PRODUCT_WEIGHT': big_product_weight,
    'INCORRECT_PRODUCT_WEIGHT': incorrect_product_weight,
    'LITTLE_PRODUCT_CALORIES': little_product_calories,
    'BIG_PRODUCT_CALORIES': big_product_calories,
    'INCORRECT_PRODUCT_CALORIES': incorrect_product_calories,
    'LITTLE_PRODUCT_PRICE': little_product_price,
    'BIG_PRODUCT_PRICE': big_product_price,
    'INCORRECT_PRODUCT_PRICE': incorrect_product_price,
    'LITTLE_RECIPE_NAME': little_recipe_name,
    'BIG_RECIPE_NAME': big_recipe_name,
    'INCORRECT_RECIPE_NAME': incorrect_recipe_name,
    'LITTLE_RECIPE_TIME': little_recipe_time,
    'BIG_RECIPE_TIME': big_recipe_time,
    'INCORRECT_RECIPE_TIME': incorrect_recipe_time,
    'LITTLE_RECIPE_TECHNOLOGY': little_recipe_technology,
    'BIG_RECIPE_TECHNOLOGY': big_recipe_technology,
    'INCORRECT_RECIPE_TECHNOLOGY': incorrect_recipe_technology,
    'INCORRECT_IMG_FORMAT': incorrect_img_format,
    'LITTLE_DISH_TYPE': little_dish_type,
    'BIG_DISH_TYPE': big_dish_type,
    'INCORRECT_DISH_TYPE': incorrect_dish_type,
    'INCORRECT_DATE_FORMAT': incorrect_date_format,
    'LITTLE_DAILYREPORT_DATE': little_dailyreport_date,
    'BIG_DAILYREPORT_DATE': big_dailyreport_date,
    'LITTLE_DAILYREPORT_COUNT': little_dailyreport_count,
    'BIG_DAILYREPORT_COUNT': big_dailyreport_count,
    'INCORRECT_DAILYREPORT_COUNT': incorrect_dailyreport_count,
    'LITTLE_DISHCOMPOSITION_COUNT': little_dishcomposition_count,
    'BIG_DISHCOMPOSITION_COUNT': big_dishcomposition_count,
    'INCORRECT_DISHCOMPOSITION_COUNT': incorrect_dishcomposition_count,
}
