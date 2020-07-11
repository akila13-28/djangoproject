from django.contrib import admin

# Register your models here.
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    card = ('id', 'Catalog', 'catagory','image', 'quesion','description')
    search_fields = ('id', 'catagory')
