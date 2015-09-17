from django.contrib import admin
from .models import Entrada, Categoria
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.

admin.site.register(Entrada, MarkdownModelAdmin)
admin.site.register(Categoria)
