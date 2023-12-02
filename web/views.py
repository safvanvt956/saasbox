from django.shortcuts import render,redirect
from . models import Update,About,Gallery_image,Award,Busines,Contact,index_portfolio_form
from . models import Email
from django.http import HttpResponse
import json
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseBadRequest



# Create your views here.

def index(request):
    if request.method == "POST":
        if request.POST.get('email5'):
            yourname = request.POST.get('name')
            email = request.POST.get('email')
            topics = request.POST.get('topics')
            message = request.POST.get('message')

        
            contact_entry = index_portfolio_form(
                yourname=yourname,
                email=email,
                topics=topics,
                message=message
            )
            contact_entry.save()

        elif request.POST.get('email_inline'):
            email = request.POST.get('email1')

            form_2 = Email(
                email=email
            )
            form_2.save()

    context = {
        'is_Home' : True
    }
    
    return render(request,'web/index.html',context)


def Updates(request):
    blog_posts = Update.objects.all()

    context = {
        'blog_posts': blog_posts,
        'is_blog1' : True
    }

    if request.method == 'POST':
        email = request.POST.get('email1')
        if email:
            Email.objects.create(email=email)
            return redirect('index')
        
    return render(request, 'web/Folder/Update.html', context)


def blogdetails1(request):
    if request.method == 'POST':
        email = request.POST.get('email1')
        if email:
            Email.objects.create(email=email)
            
        return redirect('index')
    return render(request, 'web/Folder/blog-details-1.html')


def Profile(request):
    about = About.objects.all()

    context = {
        'stand': about,
        'is_Profile' :True
    }

    if request.method == 'POST':
        email = request.POST.get('email1')
        if email:
            Email.objects.create(email=email)
            
        return redirect('index')
    return render(request,'web/Folder/Profile.html',context)



def Business_Sector(request):
    sector_posts = Busines.objects.all()

    context = {
        'three': sector_posts,
        'is_servicestandard' : True
    }
    if request.method == 'POST':
        email = request.POST.get('email1')
        if email:
            Email.objects.create(email=email)
            
        return redirect('index')
    
    return render(request,'web/Folder/Business-Sector.html',context)  




def Awards(request):
    if request.method == 'POST':
        email = request.POST.get('email1')
        if email:
            Email.objects.create(email=email)
            
        return redirect('index')
    
    service_posts = Award.objects.all()

    context = {
        'two': service_posts,
        'is_Award' : True
    }
    return render(request,'web/Folder/Award.html',context)




def contact(request):
    if request.method == "POST":
        if request.POST.get('email5'):
            fullname = request.POST.get('name')
            email = request.POST.get('email')
            topics = request.POST.get('topics')
            message = request.POST.get('message')

            contact_entry = Contact(
                fullname=fullname,
                email=email,
                topics=topics,
                message=message
            )
            contact_entry.save()
        elif request.method == 'POST':
            email = request.POST.get('email1')
            if email:
                Email.objects.create(email=email)
            
        return redirect('index')
            
    context = {
        'is_contact' : True
    }

    return render(request, 'web/Folder/Contact.html',context)



def Gallery(request):

    if request.method == 'POST':
        email = request.POST.get('email1')
        if email:
            Email.objects.create(email=email)
            
        return redirect('index')
    
    gallery_posts = Gallery_image.objects.all()

    

    context = {
        'galleries': gallery_posts ,
        'is_Gallery' : True
    }
    return render(request, 'web/Folder/Gallery.html', context)





