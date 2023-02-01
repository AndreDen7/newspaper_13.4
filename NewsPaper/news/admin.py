from django.contrib import admin
from .models import Post, Author, PostCategory, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'dateCreation', 'title', 'rating')
    list_filter = ('author',)
    search_fields = ('author', 'post_variety',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Category)
