from django.contrib import admin

# Register your models here.
from recipes.models.ingredient import Ingredient
from recipes.models.recipe import Recipe
from recipes.models.recipe_ingredient_unit import RecipeIngredientUnit
from recipes.models.tag import Tag
from recipes.models.unit import Unit

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
admin.site.register(Articles)
admin.site.register(Anonces)

class ClientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, ClientAdmin)

class ArticlesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Articles, ArticlesAdmin)

class CommandeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Commande, CommandeAdmin)

class AvisAdmin(admin.ModelAdmin):
    pass
admin.site.register(Avis, AvisAdmin)