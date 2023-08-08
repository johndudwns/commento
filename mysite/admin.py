from django.contrib import admin
from .models import MainContent, Comment

@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'image','content', 'pub_date']
    search_fields = ['title']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']


# Register your models here.
admin.site.unregister(MainContent)
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)
