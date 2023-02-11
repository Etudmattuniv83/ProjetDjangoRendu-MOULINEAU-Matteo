"""lp2023 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from recipes.views.index import IndexView
from recipes.views.register_form import RegisterFormView
from recipes.views.json.recipe_list import RecipeListJsonView
from recipes.views.recipe.recipe_detail import RecipeDetailView
from recipes.views.recipe.recipe_list import RecipeListView
from recipes.views.recipe.recipe_search import RecipeSearchView
from recipes.views.recipe.recipe_search_by_ingredient import RecipeSearchByIngredientView
from recipes.views.tag.tag_create import TagCreateView
from recipes.views.tag.tag_detail import TagDetailView
from recipes.views.tag.tag_list import TagListView
from recipes.views.tag.tag_update import TagUpdateView
from views import singup

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('recipes/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipes/detail/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/search/<str:search>', RecipeSearchView.as_view(), name='recipe_search'),
    path('recipes/search/by-ingredient/<str:search>', RecipeSearchByIngredientView.as_view(),
         name='recipe_search_by_ingredient'),
    path('tag/list', TagListView.as_view(), name='tag_list'),
    path('tag/list/detail/<int:pk>', TagDetailView.as_view(), name='tag_detail'),
    path('tag/create', TagCreateView.as_view(), name='tag_create'),
    path('tag/update/<int:pk>', TagUpdateView.as_view(), name='tag_update'),
    path('json/recipes/list', RecipeListJsonView.as_view(), name='recipe_list_json'),
    path('register', RegisterFormView.as_view(), name='recipe'),
]
