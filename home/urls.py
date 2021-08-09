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
    path('disclosure/', views.disclosure, name='disclosure'),
    path('privacy-policy/', views.privacyPolicy, name='privacyPolicy'),
    path('site-terms/', views.siteTerms, name='siteTerms'),
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
    path("ads.txt", TemplateView.as_view(
        template_name="ads.txt", content_type="text/plain")),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),

    # redirect posts
    path('top-45-most-used-git-commands-and-their-uses/', RedirectView.as_view(
        url='/blog/must-know-git-commands-and-their-uses', permanent=True)),
    path('install-wordpress-in-digitalocean-with-phpmyadmin-and-ssl/', RedirectView.as_view(
        url='/blog/how-to-install-wordpress-in-digitalocean-with-one-click-droplet-and-phpmyadmin', permanent=True)),
    path('set-up-vs-code-for-c-and-python-programming/', RedirectView.as_view(
        url='/blog/how-to-set-up-vscode-for-python-programming', permanent=True)),
    path('top-10-5g-gaming-smartphones-for-pubg-mobile-india/',
         RedirectView.as_view(url='/blog/general')),
    path('battlegrounds-mobile-india-coming-very-soon-check-release-date-here/',
         RedirectView.as_view(url='/blog/general', permanent=True)),
    path('10-best-earphones-under-500/',
         RedirectView.as_view(url='/blog/general')),
    path('best-pc-build-under-rs-35000-ryzen-3-3200g-setup/', RedirectView.as_view(
        url='/blog/best-pc-build-under-35000-ryzen-3-3200g-setup', permanent=True)),
    path('20-best-applications-for-windows-10/', RedirectView.as_view(
        url='/blog/20-best-applications-for-windows-10', permanent=True)),
    path('5-best-wi-fi-routers-under-1000/',
         RedirectView.as_view(url='/blog/general')),
    path('iphone-12-series-arrives-with-5g/',
         RedirectView.as_view(url='/blog/general', permanent=True)),
    path('how-to-create-a-bootable-usb-drive-for-windows-10/', RedirectView.as_view(
        url='/blog/how-to-create-bootable-usb-for-windows-10', permanent=True)),
    path('how-to-share-files-from-iphone-to-pc-or-android/', RedirectView.as_view(
        url='/blog/how-to-share-files-from-ios-device-to-windows-pc-or-android-devices', permanent=True)),
    path('microsoft-alerts-all-android-users-of-ransomware/', RedirectView.as_view(
        url='/blog/random-password-generator-in-python', permanent=True)),
    path('coloros-11-best-features-and-eligible-devices/',
         RedirectView.as_view(url='/blog/development', permanent=True)),
    path('create-windows-10-bootable-usb-in-ubuntu/', RedirectView.as_view(
        url='/blog/how-to-create-windows-10-bootable-usb-in-ubuntu-and-fedora', permanent=True)),
    path('nvidia-geforce-rtx-3080-a-disappointing-hype/',
         RedirectView.as_view(url='/blog/general', permanent=True)),

    # redirect pages
    path('about-us/', RedirectView.as_view(url='/about', permanent=True)),
    path('contact-us/', RedirectView.as_view(url='/contact', permanent=True)),
    path('site-blueprint/',
         RedirectView.as_view(url='/blog/development', permanent=True)),

    # redirect categories
    path('category/general/',
         RedirectView.as_view(url='/blog/general', permanent=True)),
    path('category/buying-guides/',
         RedirectView.as_view(url='/blog/general', permanent=True)),
    path('category/cheatsheet/',
         RedirectView.as_view(url='/blog/cheatsheets', permanent=True)),
    path('category/computer-science/',
         RedirectView.as_view(url='/blog/development', permanent=True)),
    path('category/how-to/',
         RedirectView.as_view(url='/blog/how-to', permanent=True)),
]
