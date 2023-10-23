from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth  import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from main.models import User

@login_required(login_url='login_url')
def index_view(request):
    active_category = Category.objects.get(is_active=True)
    context = {
        'banner': Banner.objects.all().order_by('-id')[:2],
        'about': About.objects.last(),
        'services': Servies.objects.all().order_by('-id')[:2],
        'r_pizza_meal': Meal.objects.all().order_by('-id')[:6],
        'l_pizza_meal': Meal.objects.all().order_by('-id')[3:6],
        'left_menu': Meal.objects.all().order_by('-id')[6:10],
        'right_menu': Meal.objects.all().order_by('-id')[10:14],
        'client': Client.objects.all().order_by('-id')[:4],
        'category': Category.objects.all().order_by('-id')[:4],
        'blog': Blog.objects.all().order_by('-id')[:3],
        'info': Info.objects.last(),
        'activite_meal' : Meal.objects.filter(category=active_category).order_by('-id')[:3]
    }
    return render(request, 'index.html', context)







def filter_meal_by_category(request, id):
    category = Category.objects.get(id=id)
    context = {
        'banner': Banner.objects.all().order_by('-id')[:2],
        'about': About.objects.last(),
        'services': Servies.objects.all().order_by('-id')[:2],
        'r_pizza_meal': Meal.objects.all().order_by('-id')[:6],
        'l_pizza_meal': Meal.objects.all().order_by('-id')[3:6],
        'left_menu': Meal.objects.all().order_by('-id')[6:10],
        'right_menu': Meal.objects.all().order_by('-id')[10:14],
        'client': Client.objects.all().order_by('-id')[:4],
        'category': Category.objects.all().order_by('-id')[:4],
        'blog': Blog.objects.all().order_by('-id')[:3],
        'info': Info.objects.last(),
        'filter_meal': Meal.objects.filter(category=category)
    }
    return render(request, 'index.html', context)


def new_contact_us(request):
    if request.method == "POST":
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         message = request.POST['message']
         Contact.objects.create(
            first_name= first_name,
            last_name=last_name,
            message=message,

         )
         return redirect("index_url")





def menu_view(request):
    # category = Category.objects.get(id=id)
    context={
        'r_pizza_meal': Meal.objects.all().order_by('-id')[:6],
        'l_pizza_meal': Meal.objects.all().order_by('-id')[3:6],
        'left_menu': Meal.objects.all().order_by('-id')[6:10],
        'right_menu': Meal.objects.all().order_by('-id')[10:14],
        # 'filter_meal': Meal.objects.filter(category=category),
    }
    return render(request,'menu.html', context)


def services_view(request):
    context={
        'services': Servies.objects.all().order_by('-id')[:2],
        'meal': Meal.objects.all().order_by('-id')[:2],
    }
    return render(request, 'services.html',context)
def blog_view(request):
    context={
        'blog': Blog.objects.all().order_by('-id')[:6],
    }
    return render(request, 'blog.html',context)


def blog_singe_view (request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog': blog,
        'blog_category': Blog_Category.objects.all().order_by('-id')[:6],
        'tags': Tag.objects.all().order_by('-id')[:8],
        'last_blogs' : Blog.objects.all().order_by ('-id')[:3],
        'comment' : Coment.objects.all()
    }
    return render(request, 'blog-single.html',context)


def contact_view(request):
    if request.method == "POST":
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         message = request.POST['message']
         email = request.POST['email']
         subject = request.POST['subject']
         Contact.objects.create(
            first_name= first_name,
            last_name=last_name,
            message=message,
            email=email,
            subect=subject,
         )
         return redirect("contact_url")
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')
def login_view(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        usr=authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request,'login.html')

def register_view(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        User.objects.create_user(
            username=username,
            password=password,
        )
        return redirect('index_url')
    return render(request,'register.html')

def create_message(request, pk):
    blog =Blog.objects.get(pk=pk)
    if request.method == "POST":
        text=request.POST['izox']
        Coment.objects.create(
            user=request.user,
            blog=blog,
            text=text,
        )
        return redirect("single_blog_url",blog.pk)


def log_out_view(request):
    logout(request)
    return redirect('login_url')



def edit_user_view(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password')
        user.username = username
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if email is not None:
            user.email = email
        if phone_number is not None:
            user.phone_number = phone_number
        if bio is not None:
            user.bio = bio
        if password is not None:
             if password == confirm_password:
                 user.set_password(password)
        user.save()
        return redirect("my_profile_url", id)
    return render(request, 'update-user.html')


def my_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'my_profile.html', context)