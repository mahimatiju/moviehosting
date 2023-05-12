from django.contrib import admin
from .models import Movie
class movieAdmin(admin.ModelAdmin):
    list_display = ("name", "discription", 'year', "image")
    list_filter = ("image", "name", 'year', "discription")
    search_fields = ('name__startswith',)
    fields = ('name', 'discription', 'year', 'image')
    list_editable = ('image',)

admin.site.register(Movie, movieAdmin)

