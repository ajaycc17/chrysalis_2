import json
import urllib
import math
from blog.models import BlogPost, Topic
from home.models import Contact
from podcasts.models import Episodes
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import INTERNAL_RESET_SESSION_TOKEN
from django.contrib.auth.mixins import UserPassesTestMixin

class MyPasswordResetView(UserPassesTestMixin, PasswordResetView):
    def test_func(self):
        return self.request.user.is_anonymous

    @property
    def success_url(self):
        redirect_to = self.request.GET.get('next')
        return redirect_to

    def form_valid(self, form):
        messages.success(self.request, 'Email has been sent')
        return super().form_valid(form)


class LoginAfterPasswordChangeView(PasswordResetConfirmView):
    @property
    def success_url(self):
        redirect_to = '/'
        return redirect_to

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed.')
        return super().form_valid(form)

    def dispatch(self, *args, **kwargs):
        self.validlink = False
        self.user = self.get_user(kwargs['uidb64'])

        if self.user is not None:
            token = kwargs['token']
            if token == self.reset_url_token:
                session_token = self.request.session.get(
                    INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token)
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        messages.error(self.request, 'Link use kar liye ho')
        return redirect('/')


def home(request):
    categories = Topic.objects.all()[:6]
    count = []
    for cat in categories:
        count.append((cat.title, BlogPost.objects.all().filter(
            category=cat, publish=True).count()))
    postCount = dict(count)
    carouselPost1 = BlogPost.objects.all().filter(
        publish=True).order_by('-timeStamp')[:1]
    carouselPost2 = BlogPost.objects.all().filter(
        publish=True).order_by('-timeStamp')[1:2]
    carouselPost3 = BlogPost.objects.all().filter(
        publish=True).order_by('-timeStamp')[2:3]
    allPosts = BlogPost.objects.all().filter(
        publish=True).order_by('-timeStamp')[3:9]
    Recommend = BlogPost.objects.all().filter(
        publish=False).order_by('-timeStamp')[:3]
    allPodcasts = Episodes.objects.all().filter(publish=True).order_by('-timeStamp')[:6]

    post = allPodcasts.first()
    add_string1 = '/embed'
    add_string2 = '?utm_source=generator'
    try:
        result = post.anchor_link.find('spotify.com')
        length_link = len('spotify.com')
        add_embed = result + length_link
        res = post.anchor_link[ : add_embed] + add_string1 + post.anchor_link[add_embed : ] + add_string2
    except:
        res = ""

    context = {'allPosts': allPosts, 'allPodcasts': allPodcasts,
               'postCount': postCount, 'topics': categories, 'embedPod': res, 'recommend': Recommend, 'carPost1' : carouselPost1, 'carPost2' : carouselPost2, 'carPost3' : carouselPost3} 
    return render(request, 'home/home.html', context)


def aboutPage(request):
    return render(request, 'home/about.html')


def contribute(request):
    return render(request, 'home/contribute.html')


def disclosure(request):
    return render(request, 'home/disclosure.html')


def privacyPolicy(request):
    return render(request, 'home/privacy-policy.html')


def siteTerms(request):
    return render(request, 'home/site-terms.html')


def contactPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if len(name) < 2 and len(phone) < 10:
            messages.warning(request, 'Please fill the details correctly')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=message)

            # Begin reCAPTCHA validation
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                contact.save()
                messages.success(request, 'Your message has been delivered.')
            else:
                messages.warning(
                    request, 'Invalid reCAPTCHA. Please try again.')

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query')

    if query is None or query == '' or len(query) > 200:
        query = 'No Results'
        context = {'query': query}
        return render(request, 'home/search.html', context)

    else:
        allPostsTitle = BlogPost.objects.filter(publish=True).filter(
            title__icontains=query)
        allPostsContent = BlogPost.objects.filter(publish=True).filter(
            content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        total = allPosts.count()

        postCount1 = len(allPosts)
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

        postCount2 = math.ceil(postCount1/no_of_posts)

        if page < postCount2:
            nxt = page + 1
        else:
            nxt = None

    allPosts = allPosts.order_by(
        '-timeStamp')[(page-1)*no_of_posts:page*no_of_posts]
    params = {'allPosts': allPosts, 'query': query,
              'prev': prev, 'nxt': nxt, 'total': total}
    return render(request, 'home/search.html', params)


def handleSignUp(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for erraneous inputs
        if len(username) > 10:
            messages.warning(request, 'Choose shorter username')
            return redirect(redirect_to)

        if not username.isalnum():
            messages.warning(request, 'Do not special symbols in username')
            return redirect(redirect_to)

        if pass1 != pass2:
            messages.warning(request, 'Passwords did not match')
            return redirect(redirect_to)

        myuser = User.objects.create_user(username, email, pass2)
        myuser.first_name = fname
        myuser.last_name = lname

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            myuser.save()
            messages.success(request, 'You are now a member')
            return redirect(redirect_to)
        else:
            messages.warning(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect(redirect_to)

    else:
        raise Http404()


def handleLogIn(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect(redirect_to)

        else:
            messages.error(request, 'Invalid credentials')
            return redirect(redirect_to)

    else:
        raise Http404()


def handleLogOut(request):
    redirect_to = request.GET.get('next')
    if redirect_to is None:
        raise Http404
    else:
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'You are now logged out')
            return redirect(redirect_to)
        else:
            raise Http404


def handleAllEdit(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        user = request.user
        username = request.POST['newusername']
        fname = request.POST['newfname']
        lname = request.POST['newlname']
        email = request.POST['newemail']

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username exists already try another')
            return redirect(redirect_to)

        if len(email) != 0 and User.objects.filter(email=email).exists():
            messages.warning(
                request, 'Your account already exists already try signing in')
            return redirect(redirect_to)

        if len(username) != 0:
            user.username = username

        if len(fname) != 0:
            user.first_name = fname

        if len(lname) != 0:
            user.last_name = lname

        if len(email) != 0:
            user.email = email

        if len(email) == 0 and len(lname) == 0 and len(fname) == 0 and len(username) == 0:
            messages.error(request, 'Empty fields not allowed')
            return redirect(redirect_to)

        messages.success(request, 'Your Details changed!')
        user.save()
        return redirect(redirect_to)

    else:
        raise Http404()


def handleEditPass(request):
    redirect_to = request.GET.get('next')
    if request.method == 'POST':
        username = request.user.username
        oldpass = request.POST['oldpass']
        pass1 = request.POST['editpass1']
        pass2 = request.POST['editpass2']
        u = User.objects.get(username=username)
        if pass1 == pass2:
            if(u.check_password(oldpass)):
                u.set_password(pass1)
                messages.success(request, 'Your password changed!')
                u.save()
                return redirect(redirect_to)

            else:
                messages.error(request, 'Old Password did not match!')
                return redirect(redirect_to)

        else:
            messages.error(
                request, 'Password confirmation did not match, try again!')
            return redirect(redirect_to)

    else:
        raise Http404()
