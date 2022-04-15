from django.contrib import admin
from .models import Movie, Comment

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment, CommentAdmin)