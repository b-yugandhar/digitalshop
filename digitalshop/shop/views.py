from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'index.html')


# def signup(request):
#     if request.method=='POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
        
#         if User.objects.filter(username=username).exists():

#             # If the username is taken, add an error message to the form
#             error = 'This username is already taken. Please choose another one.'
#             context = {'error': error}
#             return render(request, 'register.html',context=context )
 
#         elif pass1 != pass2:
#             return HttpResponse('password did not match')
#         else:
#             my_user = User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')

#     return render(request,'signup.html')

# def loginView(request):
#     if request.method=='POST':
#         username= request.POST.get('username')
#         pass1=request.POST.get('password')
#         user = authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')

#         else:
#             return HttpResponse('user login or password is not correct')
#     return render(request,'login.html')
# def signup(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if User.objects.filter(username=username).exists():
#             error="username again exsist"
#             context={
#                 'error':error
#             }
#             return render(request,'signup.html',context=context)

#         if pass1 != pass2:
#             error="password not matching"
#             context={
#                 'error':error
#             }
#             return render(request,'signup.html',context=context)
        
#         user_name = User.objects.create_user(username,email,pass1)
#         user_name.save()
#         return redirect('login')
#     return render(request,'signup.html')

def signupview(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            error="user already exists try differnt username"
            context={
                'error':error
            }
            return render(request,'signup.html',context=context)
        if pass1 != pass2:
            error="password not matching"
            context={
                'error':error
            }
            return render(request,'signup.html',context=context)
        user_name=User.objects.create_user(username,email,pass1)
        user_name.save()
        return redirect('login')
    
    return render(request,'signup.html')
# def loginView(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user= authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             error="username or password not right"
#             context={
#                 'error':error
#             }
#             return render(request,'login.html',context=context)
#     return render(request,'login.html')




def loginView(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error="user or password not matching"
            context={
                'error':error
            }
            return render(request,'login.html',context=context)
    return render(request,'login.html')