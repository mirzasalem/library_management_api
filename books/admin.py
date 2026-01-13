from django.contrib import admin
from .models import  Book, Category
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Book)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # show these columns

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    # list_filter = ('category',)
    # search_fields = ('title', 'author')