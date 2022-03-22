from django.contrib.sitemaps import Sitemap
from blog.models import BlogPost
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.timeStamp

    def location(self, obj):
        return '/blog/%s' % (obj.slug)


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return ['home:home', 'home:aboutPage', 'home:contactPage', 'home:contribute', 'home:disclosure', 'home:privacyPolicy', 'home:siteTerms']

    def location(self, item):
        return reverse(item)
