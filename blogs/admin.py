from django.contrib import admin
from  .models import Category,Blog, SocialLink
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','get_category_name', 'author', 'status', 'is_featured']
    search_fields = ('id', 'title', 'Category__category_name', 'status')
    list_editable = ('is_featured',)

    def get_category_name(self, obj):
        return obj.Category.category_name

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SocialLink)