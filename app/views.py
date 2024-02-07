from django.shortcuts import render

# Create your views here.

from app.forms import *

# from app.models import user
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from app.models import User



# @login_required
def registerform(request):

    uf = user_form()
    upf =user_profile_form()

    if request.method == 'POST' and request.FILES:

        ufd = user_form(request.POST)
        UPFD = user_profile_form(request.POST,request.FILES)

        if ufd.is_valid() and UPFD.is_valid():
            pw = ufd.cleaned_data['password']
            user_form_data_object = ufd.save(commit=False)
            user_form_data_object.set_password(pw)

            user_form_data_object.save()
        
            user_profile_data_form = UPFD.save(commit=False)

            user_profile_data_form.user = user_form_data_object

            user_profile_data_form.save()

            return HttpResponse("data saved successfully")

    return render(request,'registerform.html',{'uf':uf,'upf':upf})



def ulogin(request):

    if request.method == 'POST':
        username = request.POST['text']
        pw = request.POST['pw']
        user = authenticate(username = username,password = pw)   

        print("the user is ",user)

        if user and user.is_active:
            

            login(request,user)

            request.session['username'] = username

            
            

            return redirect('profile_page')



    return render(request,'user_login.html')


@login_required
def profile_page(request):


    user  = request.session.get('username')
    print(user)



    UO = User.objects.get(username=user)

    UPO = user_profile.objects.get(user = UO)


    if request.method == 'POST':
        logout(request) 

        return HttpResponse("logout successfull")


    return render(request,'user_details.html',{'user':user,'UO':UO,'UPO':UPO})



