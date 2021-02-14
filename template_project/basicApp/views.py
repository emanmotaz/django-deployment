from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from basicApp.forms import UserForm,UserProfileInfoForm


# login
from django.urls import reverse
# use when the view must be shown only for authurizaed users
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    dict = {'text':'Hello World','number':100}
    return render(request,'basic_app/index.html',dict)
def basic(request):
    return render(request,'basic_app/basic.html')
def other(request):
    return render(request,'basic_app/other.html')
def relative(request):
    return render(request,'basic_app/relative_urls_templates.html')
def register(request):
    registered = False
    if request.method == 'POST':
        user_form  = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            # not save it yet but for the relation ship
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors ,profile_form.errors)
    else:
        user_form  = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'basic_app/registeration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not active")
        else:
            print('someones Login Failed')
            print('name : {} , password:{}'.format('username','password'))
            return HttpResponse("Invalid")
    else:
        return render(request,'basic_app/login.html')
# Any def will be decorated with @login_required the user cant access it unless
# he is logged in
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required
def special(request):
    return ttpResponse("You Are Logged in")
