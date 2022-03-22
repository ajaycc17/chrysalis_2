from django.http.response import Http404
from django.shortcuts import render, redirect
from blog.models import BlogPost, BlogComment, Topic
from django.contrib import messages
import math
import random


def topics(request):
    categories = Topic.objects.all()
    count = []
    for cat in categories:
        count.append((cat.title, BlogPost.objects.all().filter(
            category=cat, publish=True).count()))
    postCount = dict(count)
    context = {'postCount': postCount, 'topics': categories}
    return render(request, 'blog/allCategory.html', context)


def blogPage(request):
    all = BlogPost.objects.all().filter(publish=True)
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

    allPosts = BlogPost.objects.all().filter(publish=True).order_by(
        '-timeStamp')[(page-1)*no_of_posts:page*no_of_posts]
    context = {'allPosts': allPosts, 'prev': prev,
               'nxt': nxt, 'total': postCount}
    return render(request, 'blog/blog.html', context)


def blogPost(request, slug):
    post = BlogPost.objects.filter(slug=slug, publish=True).first()
    categories = Topic.objects.all().filter(title=slug).first()
    catpost = BlogPost.objects.all().filter(category=categories, publish=True)
    authpost = BlogPost.objects.all().filter(author=slug, publish=True)
    author = slug
    # recommendation
    try:
        recommend = BlogPost.objects.all().filter(publish=True).exclude(slug=slug).order_by('-likes', '-timeStamp')[:5]
    except:
        recommend = BlogPost.objects.all().filter(publish=True).exclude(slug=slug).order_by('-likes', '-timeStamp')

    # if any post exists
    if post:
        # reading time calculation: 250 word per minute
        content = post.content
        res = len(content.split())
        readTime = math.ceil(res/250)
        # comments
        comments = BlogComment.objects.filter(
            post=post, parent=None).order_by('-timeStamp')
        replies = BlogComment.objects.filter(post=post).exclude(
            parent=None).order_by('-timeStamp')
        repDict = {}
        for reply in replies:
            if reply.parent.sno not in repDict.keys():
                repDict[reply.parent.sno] = [reply]
            else:
                repDict[reply.parent.sno].append(reply)

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
        
        topics = Topic.objects.all()

        context = {'post': post, 'comments': comments, 'user': request.user,
                   'repDict': repDict, 'recommended': recommend, 'readTime': readTime, 'nextPost':BlogPost.objects.all().filter(sno = n).first(), 'prevPost':BlogPost.objects.all().filter(publish=True, sno = p).first(), 'topics':topics}
        return render(request, 'blog/blogPost.html', context)

    elif catpost.count() != 0:
        postCount1 = len(catpost)
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

        pageCount = math.ceil(postCount1/no_of_posts)

        if page < pageCount:
            nxt = page + 1
        else:
            nxt = None

        contextCat = {'allPosts': catpost.order_by(
            '-timeStamp')[(page-1)*no_of_posts:page*no_of_posts], 'prev': prev, 'nxt': nxt, 'total': postCount1, 'topics': categories}
        return render(request, "blog/category.html", contextCat)

    elif authpost.count() != 0:
        postCount1 = len(authpost)
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

        pageCount = math.ceil(postCount1/no_of_posts)

        if page < pageCount:
            nxt = page + 1
        else:
            nxt = None

        contextCat = {'allPosts': authpost.order_by(
            '-timeStamp')[(page-1)*no_of_posts:page*no_of_posts], 'prev': prev, 'nxt': nxt, 'total': postCount1, 'topics': author}
        return render(request, "blog/author.html", contextCat)

    else:
        raise Http404()


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = BlogPost.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(request, 'Comment posted')

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)
            messages.success(request, 'Reply posted')

        comment.save()
        return redirect(f"/blog/{post.slug}")

    else:
        raise Http404()
