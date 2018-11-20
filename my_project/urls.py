"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from offside.views import IndexView,LeagueView,\
    FixtureView,ContactView,LeagueDetail,\
    FixtureDetail,Fixture,NewsView,ShopView,ChartView,\
    ReportView,SignUp,PlayerView,NewsDetail,ShopDetail
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include



urlpatterns = [
    url(r'^$',IndexView.as_view(),name="index"),
    # url(r'^league/premier$',LeagueView.as_view(),name="league"),
    url(r'^league/(?P<slug>[\w-]+)/$',LeagueDetail.as_view(),name="leaguedetail"),
    url(r'^fixture/$',FixtureView.as_view(),name="fixture"),
    url(r'^fixture/(?P<slug>[\w-]+)/$',FixtureDetail.as_view(),name="fixturedetail"),
    url(r'^player/(?P<slug>[\w-]+)/$',PlayerView.as_view(),name="player"),
    url(r'^fixture/(?P<slug>[\w-]+)/(?P<nth>[\w-]+)/$',Fixture.as_view(),name="fixtures"),
    url(r'^contact/$',ContactView.as_view(),name="contact"),
    url(r'^news/$',NewsView.as_view(),name="news"),
    url(r'^news/(?P<slug>[\w-]+)/$',NewsDetail.as_view(),name="newsdetail"),
    url(r'^shop/$',ShopView.as_view(),name="shop"),
    url(r'^shop/(?P<slug>[\w-]+)/$',ShopDetail.as_view(),name="shopdetail"),
    url(r'^shop/chart$',ChartView.as_view(),name="chart"),
    url(r'^report/$',ReportView.as_view(),name="report"),
    url('accounts/', include('django.contrib.auth.urls')),
    url('signup/', SignUp.as_view(), name='signup'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

