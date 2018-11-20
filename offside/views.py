# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import  TemplateView,ListView,DetailView,FormView
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Team,League,Manager,Match,News,Product

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import CommentModelForm,CommentNewsForm




class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



class IndexView(TemplateView):

    template_name = "index.html"

class ContactView(TemplateView):

    template_name = "contact.html"

class LeagueView(ListView):

    queryset = Team.objects.filter(League=1).order_by('-point')
    template_name = "league.html"

class LeagueDetail(ListView):


        template_name = "league.html"

        def get_queryset(self, *args, **kwargs):
            slug = self.kwargs.get("slug")
            league = League.objects.get(slug=slug)
            return Team.objects.filter(League=league.id).order_by('-point')



class ShopView(ListView):

    model = Product
    template_name = "shop.html"
    context_object_name = 'object_list'
    queryset= Product.objects.all()




class NewsView(ListView):
    model = News
    template_name = "news.html"
    context_object_name = 'object_list'
    paginate_by = 3
    queryset = News.objects.all()


class NewsDetail(ListView,FormView):
    context_object_name = 'object_list'
    template_name = "news_detail.html"
    form_class = CommentNewsForm
    success_url = '/'

    def get_object(self):
        slug = self.kwargs.get("slug")
        return News.objects.get(slug=slug)


    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        news= News.objects.get(slug=slug)
        print(news)
        return News.objects.filter(id=news.id)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.news = self.get_object()
        comment.user=self.request.user
        comment.rating = form.cleaned_data['rating']
        comment.save()
        return super(NewsDetail, self).form_valid(form)

class ShopView(ListView):

    model = Product
    template_name = "shop.html"
    context_object_name = 'object_list'
    paginate_by = 6
    queryset= Product.objects.all()


class ShopDetail(ListView,FormView):

    template_name = "shop_detail.html"
    form_class = CommentModelForm
    success_url = '/'


    def get_object(self):
        slug = self.kwargs.get("slug")
        return Product.objects.get(slug=slug)

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        product= Product.objects.get(slug=slug)
        return Product.objects.filter(id=product.id)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.product = self.get_object()
        comment.user=self.request.user
        comment.rating = form.cleaned_data['rating']
        comment.save()
        return super(ShopDetail, self).form_valid(form)

class FixtureView(ListView):
    queryset = Match.objects.filter(away_team__League=1)
    template_name = "fixture.html"



class FixtureDetail(ListView):

        template_name = "fixture.html"

        def get_queryset(self, *args, **kwargs):
            slug = self.kwargs.get("slug")
            league = League.objects.get(slug=slug)
            print (league)
            return Match.objects.filter(away_team__League =league.id)

class Fixture(ListView):

        template_name = "fixture.html"

        def get_queryset(self, *args, **kwargs):
            slug = self.kwargs.get("slug")
            nth = self.kwargs.get("nth")
            league = League.objects.get(slug=slug)
            return Match.objects.filter(away_team__League =league.id,nth=nth)


class PlayerView(ListView):
    template_name = "players.html"
    context_object_name = "leplayer"

    def get_queryset(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        name = self.kwargs.get("name")
        team = Team.objects.get(slug=slug)
        return team






class ChartView(TemplateView):

    template_name = "chart.html"


class ReportView(TemplateView):

    template_name = "report.html"



