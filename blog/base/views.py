
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from . models import Blog
from . forms import BlogForm
from django.shortcuts import get_object_or_404


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
    
            
            return render(request,'home2.html')
            
        else:
            
            return redirect('home2')
        
            

    
    return render(request, "login.html")
            
            


def Signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        myuser = User.objects.create_user(username, email, password)
        

        myuser.save()

        messages.success(request,"your account has been sucessfully  created")

        return redirect('login')
    return render(request,"signup.html")



def Home(request):
    if request.method == "POST":
        return redirect('features')

    
    
    return render(request,"home.html")


def Features(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        T = Blog.objects.create(title = title,description = description)
        T.save()

        return redirect('myblogs')
    return render(request,"features.html")


def Myblogs(request):
    
    return render(request,"myblogs.html")


def Aboutus(request):
    return render(request,"aboutus.html")

def Aboutus2(request):
    return render(request,"aboutus2.html")

def Delete(request,id):
    context = {}
    obj = get_object_or_404(Blog,id=id)
    if request.method=="POST":
        obj.delete()
        return redirect("myblogs2")


    return render(request,"delete.html",context)


def Update(request,id):
    context= {}
    obj = get_object_or_404(Blog,id=id)
    form = BlogForm(request.POST or None , instance=obj )

    if form.is_valid():
        form.save()

        return redirect('myblogs')
    context['form']=form


    

    return render(request, "Update.html", context)



def Myblogs2(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request,"myblogs2.html",context)


def Features2(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        T = Blog.objects.create(title = title,description = description)
        T.save()

        return redirect('myblogs2')
    return render(request,"features2.html")



def Home2(request):
    if request.method == "POST":
        return redirect('features2')
    
    
    
    
    return render(request,"home2.html")




    