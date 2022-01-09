from django.http.response import Http404
from django.shortcuts import render, redirect
from podcasts.models import Episodes
from django.contrib import messages
import math


def podcastsHome(request):
    all = Episodes.objects.all().filter(publish=True)
    postCount = len(all)
    no_of_posts = 12
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    if page > 1:
        prev = page - 1
    else:
        prev = None

    page_count = math.ceil(postCount/no_of_posts)

    if page < page_count:
        nxt = page + 1
    else:
        nxt = None

    allPosts = Episodes.objects.all().filter(publish=True).order_by(
        '-timeStamp')[(page-1)*no_of_posts:page*no_of_posts]
    context = {'allPosts': allPosts, 'prev': prev,
               'nxt': nxt, 'total': postCount}
    return render(request, 'podcasts/index.html', context)

def singlePodcast(request, slug):
    post = Episodes.objects.filter(slug=slug, publish=True).first()
    add_string1 = '/embed'
    add_string2 = '?utm_source=generator'
    result = post.anchor_link.find('spotify.com')
    length_link = len('spotify.com')
    add_embed = result + length_link
    res = post.anchor_link[ : add_embed] + add_string1 + post.anchor_link[add_embed : ] + add_string2

    # recommendation
    try:
        recommend = Episodes.objects.all().filter(publish=True).exclude(slug=slug).order_by('-likes', '-timeStamp')[:5]
    except:
        recommend = Episodes.objects.all().filter(publish=True).exclude(slug=slug).order_by('-likes', '-timeStamp')

    # if any post exists
    if post:
        if (request.POST.get('liker', 'off')) == 'on':
            redirect_to = request.POST.get('path')
            post.likes += 1
            post.save()
            return redirect(redirect_to)

        elif request.POST.get('disliker', 'off') == 'on':
            redirect_to = request.POST.get('path')
            return redirect(redirect_to)

        try:
            p = post.sno - 1
            n = post.sno + 1
        except:
            pass

        context = {'post': post, 'res': res, 'user': request.user, 'recommended': recommend, 'nextPost':Episodes.objects.all().filter(sno = n).first(), 'prevPost':Episodes.objects.all().filter(publish=True, sno = p).first()}
        return render(request, 'podcasts/singlePodcast.html', context)
    else:
        raise Http404()