
import pdb
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Register
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# from django.core.paginator import Paginator
from .forms import form_class
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register_view(request):
    #get the paramaters.
    if request.method=="POST":
        name=request.POST['nm']
        email=request.POST['em']
        username=request.POST['uname']
        password=request.POST['pswd']
        confirmpassword=request.POST['cnpswd']


        #va lidations.
        if len(name)>10:
            messages.error(request,'username must be under 10 character')
            return redirect('register')

        if not name.isalpha():
            messages.error(request,'username should only contain 10 characters')
            return redirect('register')


        if password!=confirmpassword:
            messages.error(request,'Confirm Password do not match with Password')
            return redirect('register')

            #create the user.....

        # import pdb;pdb.set_trace()
        createuser = User.objects.create_user(username,email,password)
        createuser.first_name=name
        createuser.save()
        messages.success(request,'user is successfully registered...')
        return redirect('login') 
    else:    
        return render(request,'register.html')




def login_view(request):
  #get the paramaters.
    if request.method=="POST":
        username=request.POST['loginuname']
        password=request.POST['loginpswd']
        # import pdb; pdb.set_trace()
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'user is successfully logged in...')
            request.session['usernameskey']=username
            request.session['passwordskey']=password 
            return redirect('index')

        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')

    else:        
        return render(request,'login.html')



def index_view(request):

    print('session username:',request.session.get('usernameskey'))
    print('session password:',request.session.get('passwordskey'))
    return render(request,'index.html')

def form_view(request):
    
    form=form_class(request.POST)
    # if request.method=="POST":

    if form.is_valid():
        if form != ' ':
            form.save()
            return redirect('login')
        else:
            return Http404


    return render(request,'index.html',{'form': form})


def usercreation_view(request):
        
        # usercreation=UserCreationForm() 
        # if request.POST=="POST":
        #     usercreation=UserCreationForm()  
        #     if usercreation.is_valid():
        #         usercreation.save()
        #         messages.success(request,'successfully registered...')
        #         return redirect('usercreationform')
        #     else:
        #         
        #         # return HttpResponse('something going wrong...!!!')    
        # return render(request,'usercreation_form.html',{'usercreation':usercreation})

        if request.method == 'POST':
            f = UserCreationForm(request.POST)
            if f.is_valid():
                f.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            f = UserCreationForm()
        return render(request, 'usercreation_form.html', {'form': f})




# print(dir(User))






