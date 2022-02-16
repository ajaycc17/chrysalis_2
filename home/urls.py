from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap, StaticSitemap
from .feeds import LatestPostsFeed
from . import views
from django.views.generic.base import TemplateView, RedirectView

sitemaps = {
    'blog': BlogSitemap,
    'static': StaticSitemap
}

urlpatterns = [
    path('', views.home, name='home'),
    path("feed/", LatestPostsFeed(), name="post_feed"),
    path('about/', views.aboutPage, name='aboutPage'),
    path('contact/', views.contactPage, name='contactPage'),
    path('contribute/', views.contribute, name='contribute'),
    path('search/', views.search, name='search'),
    path('signup/', views.handleSignUp, name='handleSignUp'),
    path('login/', views.handleLogIn, name='handleLogIn'),
    path('logout/', views.handleLogOut, name='handleLogOut'),
    path('editpass/', views.handleEditPass, name='handleEditPass'),
    path('editdetprofile/', views.handleAllEdit, name='handleAllEdit'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('reset-password/', views.MyPasswordResetView.as_view(),
         name='password_reset'),
    path('set-password/<slug:uidb64>/<slug:token>/',
         views.LoginAfterPasswordChangeView.as_view(), name='password_reset_confirm'),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),

    # redirect pages
    path('about-us/', RedirectView.as_view(url='/about', permanent=True)),
    path('contact-us/', RedirectView.as_view(url='/contact', permanent=True)),
]
