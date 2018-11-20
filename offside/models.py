# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from django.utils.text import slugify



from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings




class Team(models.Model):

    name = models.CharField(max_length=30)
    point = models.IntegerField()
    played_match = models.IntegerField()
    win = models.IntegerField()
    lost = models.IntegerField()
    draw = models.IntegerField()
    average = models.IntegerField()
    League = models.ForeignKey('League',
        on_delete=models.CASCADE,)
    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Team, self).save()

    def __str__(self):

        return self.name

class League(models.Model):

    name = models.CharField(max_length=30)

    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(League, self).save()


    def __str__(self):

        return self.name


class Manager(models.Model):
    Team = models.ForeignKey('Team',on_delete=models.CASCADE,related_name="managers" )
    League = models.ForeignKey('League', on_delete=models.CASCADE, )
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to= "static/img/staff/manager", blank=True)

    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Manager, self).save()



    def __str__(self):

        return self.name

class Player(models.Model):


    Team = models.ForeignKey('Team',on_delete=models.CASCADE,related_name="players" )
    name = models.CharField(max_length=30)
    number = models.IntegerField(default=5)
    position = models.CharField(max_length=30,default='Defender')
    pic = models.ImageField(upload_to= "static/img/staff/player", blank=True)
    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super (Player,self).save()


    def __str__(self):

        return self.name

class Match(models.Model):

    nth = models.IntegerField(default=1)
    date = models.DateField()
    hour = models.TimeField()
    home_team = models.ForeignKey('Team',on_delete=models.CASCADE, related_name="matchhome" )
    away_team = models.ForeignKey('Team',on_delete=models.CASCADE, related_name="matchaway")
    stadium = models.CharField(max_length=50)
    result = models.CharField(max_length=10,default='1-1',blank=True)

    def __str__(self):

        template = '{0.nth} {0.home_team} {0.away_team}'
        return template.format(self)

    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.home_team, self.away_team)
        super(Match, self).save()





class News(models.Model):

    title = models.CharField(max_length=75)
    desc = models.TextField(max_length=1000)
    date = models.DateField()
    pic = models.ImageField(upload_to="static/img/news", blank=True)
    category = models.CharField(max_length=30)
    League = models.ForeignKey('League',
        on_delete=models.CASCADE,)
    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(News, self).save()

    def __str__(self):

        return self.title



class Product(models.Model):
    title=models.CharField(max_length=50,blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, )
    size = models.CharField(max_length=10)
    colour =models.CharField(max_length=20)
    price =models.IntegerField()
    Team = models.ForeignKey('Team', on_delete=models.CASCADE, )
    pic = models.ImageField(upload_to="static/img/product", blank=True)
    slug = models.SlugField(editable=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Product, self).save()

    def __str__(self):

        return  self.title

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):

        return  self.title

class Comment(models.Model):

    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

class CommentNews(models.Model):
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

