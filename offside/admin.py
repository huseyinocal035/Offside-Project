# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Team,Category,League,Manager,Player,Match,News,Product,Comment,CommentNews

admin.site.register(Team)
admin.site.register(League)
admin.site.register(Manager)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(News)
admin.site.register(Product)
admin.site.register(Category)

class CommentAdmin(admin.ModelAdmin):
  model = Comment
  list_display = ['id', 'title', 'product', 'rating']

admin.site.register(Comment, CommentAdmin)


class CommentNewsAdmin(admin.ModelAdmin):
  model = CommentNews
  list_display = ['user', 'title', 'news', 'rating']

admin.site.register(CommentNews, CommentNewsAdmin)


