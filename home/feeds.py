from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.template.defaultfilters import truncatewords
from blog.models import BlogPost
from django.urls import reverse
from datetime import date


class LatestPostsFeed(Feed):
    feed_type = Atom1Feed
    title = "OrbitGadget Blog Feed"
    link = "/"
    subtitle = "All posts of the blog."

    def items(self):
        return BlogPost.objects.all()

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse("BlogPost", args=[item.slug])

    def item_author_name(self, item):
        return item.author

    def item_description(self, item):
        return truncatewords(item.content, 33)

    def feed_copyright(self):
        return f'Copyright (c) 2020-{date.today().year}, OrbitGadget'
