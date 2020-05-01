from django.shortcuts import render
from register_app.forms import UserForm,UserProfileInfoForm

#imports require for login
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required



# Create your views here.
#Home page view
def index(request):
    return render(request,"register_app/index.html")

#for logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



#Register page view
def register(request):
    registered=False

    if request.method=="POST":
        user_form = UserForm(data=request.POST)  #tag for UserForm
        profile_form = UserProfileInfoForm(data=request.POST) #tag for UserProfileInfoForm


        #check for validation of input provided by user
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()  #save to the Database
            user.set_password(user.password)  #hash the password
            user.save()  #save the hash password in the databases

            profile=profile_form.save(commit=False) #dont commit data to the databases
            profile.user=user     #for one to one relationship

            if 'profile_pic' in request.FILES:
                print("Under profile pic")
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()    #update data to the Database

            registered=True

        else:    #in case if there is error in validation of input data
            print(user_form.errors,profile_form.errors)
    else:      #in case if the method is not post
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    context_dic={"user_form":user_form,"profile_form":profile_form,"registered":registered}
    return render(request,"register_app/register.html",context_dic)




#login views

def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("<h3>Account is not active</h3>")

        else:
            #print will print the stuff on the console
            print("Someone try to login in your account")
            print("Entered Username:{} and Password:{}".format(username,password))
            return HttpResponse("<h2>Invalid Username or Password</h2>")

    else:
        return render(request,"register_app/login.html",{})
