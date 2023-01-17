from django.urls import path
from main_app.views import LoadMainPage,\
        LoadAddProdPage,\
        LoadLookProdPage,\
        LoadEditProdPage,\
        LoadAddRecipePage,\
        LoadLookRecipePage,\
        LoadEditRecipePage,\
        LoadAddDishPage,\
        LoadLookDishPage,\
        LoadEditDishPage,\
        LoadLookDishcompositionPage,\
        LoadAddDishcompositionPage,\
        LoadEditDishcompositionPage,\
        LoadAddDailyReportPage,\
        LoadLookGlobalDailyReportPage,\
        LoadLookLocalDailyReportPage,\
        LoadEditDailyReportPage

urlpatterns = [
        path('', LoadMainPage, name='main_page'),
        path('add/product', LoadAddProdPage, name='add_prod'),
        path('look/product', LoadLookProdPage, name='look_prod'),
        path('edit/product', LoadEditProdPage, name='edit_prod'),
        path('add/recipe', LoadAddRecipePage, name='add_recipe'),
        path('look/recipe', LoadLookRecipePage, name='look_recipe'),
        path('edit/recipe', LoadEditRecipePage, name='edit_recipe'),
        path('add/dish', LoadAddDishPage, name='add_dish'),
        path('look/dish', LoadLookDishPage, name='look_dish'),
        path('edit/dish', LoadEditDishPage, name='edit_dish'),
        path('look/dishcomposition', LoadLookDishcompositionPage, name='look_dishcomposition'),
        path('add/dishcomposition', LoadAddDishcompositionPage, name='add_dishcomposition'),
        path('edit/dishcomposition', LoadEditDishcompositionPage, name='edit_dishcomposition'),
        path('add/dailyreport', LoadAddDailyReportPage, name='add_dailyreport'),
        path('look/globaldailyreport', LoadLookGlobalDailyReportPage, name='look_global_dailyreport'),
        path('look/localdailyreport', LoadLookLocalDailyReportPage, name='look_local_dailyreport'),
        path('edit/dailyreport', LoadEditDailyReportPage, name='edit_dailyreport'),
        ]
