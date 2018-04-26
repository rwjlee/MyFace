from django.shortcuts import render, redirect
import apps.user_info.models as m
from django.contrib import messages
from django.db.models import Q, Count, Sum, Max

# Create your views here.
def index(request):
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
        'results': results
    }
    return render(request, 'user_info/search_results.html', context)

def add_follows(request):
    # if m.Follow.objects.get(Q(follower_id = htm_follower) & % Q(following_id = html_following))



def following_page(request):
    if 'user_id' not in request.session:
        return redirect('user_info:login')

    user_id = request.session['user_id']
    followings = m.Follow.objects.values('following_id').filter(follower_id = user_id)
    print(type(followings))

    context = {
        'followings': followings
    }
    return render(request, 'user_info/following_page.html', context)

def login(request):
    if request.method == 'POST':
        html_email = request.POST['html_email']
        html_password = request.POST['html_password']
        try:
            user = m.User.objects.get(email = html_email)
            if user.password == html_password:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
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