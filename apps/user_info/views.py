from django.shortcuts import render, redirect
import apps.user_info.models as m
from django.contrib import messages
from django.db.models import Q, Count, Sum, Max

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('user_info:user_page', user_id=request.session['user_id'])

    return render(request, 'user_info/index.html')

def search(request):
    html_term = request.GET['html_term']

    if len(html_term)>0:
        return redirect('user_info:search_results', term = html_term)
    else:
        return render(request, 'user_info/search_results.html', None)

def search_results(request, term):

    results = m.User.objects.filter(Q(email__icontains = term) | Q(username__icontains=term))
    context = {
        'results': results,
    }
    return render(request, 'user_info/search_results.html', context)

def add_follow(request, following_id):

    if 'user_id' not in request.session:
        return redirect('user_info:login')

    html_user = request.session['user_id']
    html_following = following_id

    print("{} is following {}".format(html_user, html_following))
    try:
        follow = m.Follow.objects.create(follower_id = html_user, following_id = html_following)
    except:
        pass
    
    return redirect('user_info:following_page')

def delete_follow(request, follow_id):
    
    follow = m.Follow.objects.get(id = follow_id)
    follow.delete()
    
    return redirect('user_info:following_page')

def follower_page(request):
    if 'user_id' not in request.session:
        return redirect('user_info:login')

    user_id = request.session['user_id']
    followers = m.Follow.objects.filter(following_id = user_id)

    context = {
        'followers': followers
    }

    return render(request, 'user_info/follower_page.html', context)

def following_page(request):
    if 'user_id' not in request.session:
        return redirect('user_info:login')

    user_id = request.session['user_id']
    followings = m.Follow.objects.filter(follower_id = user_id)

    context = {
        'followings': followings
    }

    print(type(followings))
    print(followings[0])

    return render(request, 'user_info/following_page.html', context)

def user_page(request, user_id):
    posts = m.Post.objects.filter(user_id = user_id)
    context = {
        'posts': posts,
        'user_id': user_id
    }
    return render(request, 'user_info/user_page.html', context)

def add_post(request):
    if request.method == 'POST':
        html_content = request.POST['html_content']
        html_user = request.session['user_id']

        if len(html_content) > 0:
            post = m.Post.objects.create(user_id = html_user, content = html_content)

    return redirect('user_info:index')
    
def delete_post(request, post_id):
    post = m.Post.objects.get(id = post_id)
    post.delete()
    return redirect('user_info:index')
    
def login(request):
    if request.method == 'POST':
        html_email = request.POST['html_email']
        html_password = request.POST['html_password']
        try:
            user = m.User.objects.get(email = html_email)
            if user.password == html_password:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                request.session['username'] = user.username
                return redirect('user_info:index')
            else:
                messages.error(request, 'Invalid Login')
                return redirect('user_info:login')

        except:
            messages.error(request, 'No such user')
            return redirect('user_info:login')

    return render(request, 'user_info/login.html')

def logout(request):
    request.session.clear()
    return redirect('user_info:index')

def register(request):
    if 'user_id' in request.session:
        return redirect('user_info:index')

    if request.method == 'POST':
        if len(request.POST['html_password']) > 0 and request.POST['html_password']==request.POST['html_confirm']:
            try:
                user = m.User.objects.create(email = request.POST['html_email'], password = request.POST['html_password'], username = request.POST['html_username'])
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                request.session['username']=user.username
            except:
                messages.error(request, 'This is wrong')
                return redirect('user_info:register')

        return redirect('user_info:index')

    return render(request, 'user_info/register.html')