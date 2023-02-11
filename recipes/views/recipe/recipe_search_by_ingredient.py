from django.db.models import Q
from django.views.generic import ListView

from recipes.models.recipe import Recipe


class RecipeSearchByIngredientView(ListView):
    template_name = 'recipe_list_view.html'

    def get_queryset(self):
        # return Recipe.objects.filter(
        #     ingredients_units__ingredient__name_singular__icontains=self.kwargs['search']
        # )
        return Recipe.objects.filter(
            Q(ingredients_units__ingredient__name_singular__icontains=self.kwargs['search']) |
            Q(ingredients_units__ingredient__name_plural__icontains=self.kwargs['search'])
        )
