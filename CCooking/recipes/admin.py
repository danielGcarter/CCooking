from django.contrib import admin
from recipes.models import Recipe, Ingredient, Category

class recipeAdmin(admin.ModelAdmin):
    pass

class ingredientAdmin(admin.ModelAdmin):
    pass

class categoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, recipeAdmin)
admin.site.register(Ingredient, ingredientAdmin)
admin.site.register(Category, categoryAdmin)
