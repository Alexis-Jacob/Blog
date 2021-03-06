from django.contrib import admin
from Blog.models import *

class   ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'validated', 'category')
    list_filter = ('author','category', 'validated')
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', ), }

class   CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name', ), }


class   CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content')

admin.site.register(FileCategory)
admin.site.register(FileUpload)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
