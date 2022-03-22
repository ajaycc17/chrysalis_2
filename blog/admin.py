from django.contrib import admin
from blog.models import BlogComment, BlogPost, Topic

admin.site.register((BlogComment))
admin.site.register((Topic))


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    class Media:
        js = ('/static/js/tinyInject.js',)
