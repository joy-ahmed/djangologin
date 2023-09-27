from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from accounts.models import UserProfile

# Create your views here.
def home(request):
    try:
        profileImg = UserProfile.objects.get(user=request.user).profileImg.url
    except:
        profileImg = ""
    return render(request, 'home.html', {"profileImg": profileImg})


def loginPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'login.html')
    else:
        return redirect('/')

def logOut(request):
    logout(request)
    return redirect('login')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = User(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = make_password(password)
            )
            user.save()

        return render(request, 'signup.html')
    else:
        return redirect('/')