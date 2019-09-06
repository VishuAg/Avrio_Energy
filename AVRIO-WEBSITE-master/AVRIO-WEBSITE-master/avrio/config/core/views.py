from django.shortcuts import render

from . import models
from core.form import NewUser
from core.models import blogmodel,newsmodel
from django.http import HttpResponse
from django.views.generic import (View,ListView,TemplateView,
                                DetailView)


# Create your views here.
'''
A view is a function that processes an HTTP request, fetches the required data from the database,
renders the data in an HTML page using an HTML template,
and then returns the generated HTML in an HTTP response to display the page to the user.
'''
def index(request):
    news_list = newsmodel.objects.order_by('date')
    news_list_three=[]
    for x in range(3):

        news_list_three.append(news_list[x])

    news_dict = {"access_records":news_list_three}
    return render(request, "index.html", context=news_dict)
def team(request):
    return render(request, "team.html",{})
def Solutions(request):
    # solutions_list = datamod.objects.order_by('index')
    #
    #
    # solutions_dict = {"access_records":solutions_list}
    return render(request, "Solutions.html")
def SmartSol(request):
    return render(request, "SmartSol.html",{})

def faq(request):
    return render(request, "faq.html",{})
def login(request):
    return render(request, "login.html",{})
def privacy(request):
    return render(request, "privacy.html",{})
def gallery(request):
    return render(request, "gallery.html",{})


def news(request):
    news_list = newsmodel.objects.order_by('date')
    news_dict = {"access_records":news_list}
    return render(request,"news.html",context=news_dict)
# def blog(request):
#
#     return render(request, "blog.html",{})

def blog(request):
    blog_list = blogmodel.objects.order_by('date')
    blog_dict = {"access_records":blog_list}
    return render(request,"blog.html",context=blog_dict)

class blogdetails(DetailView):
    context_object_name = 'blog_details'
    model = models.blogmodel
    template_name = "blogdetails.html"



def aboutus(request):
    return render(request, "about_us.html",{})
def userdata(request):
    form=NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error from invalid')
    return render(request,'contact.html',{})

def contact(request):
    return render(request, "contact.html",{})
def login(request):
    return render(request, "login.html",{})
