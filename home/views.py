from django.shortcuts import render, HttpResponse
from datetime import datetime
from matplotlib.pyplot import title

from requests import post
from home.models import Contact
from django.contrib import messages            # to flash a message while user submits the form on the site

# Create your views here.
def index(request):
    context = {
        'variable':'This is sent!!!'
    }
    #return HttpResponse(" This is the Home page 😊.")
    return render(request, 'index.html', context)

# we can create as many functions as we want to get the desired 

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page 😍")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("These are the services offered 😁")
    # MAKE THE REQUIRED CHANGES FOR THREE PAGES OF THE DROP DOWN MENU FOR THE SERVICES PAGE

def services1(request):
    return render(request, 'services1.html')

def services2(request):
    return render(request, 'services2.html')

def services3(request):
    return render(request, 'services3.html')


def contact(request):
    # to get posted info on the page in the database we can write this logic
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Thanks for reaching us you will soon be contacted 😊')   # to flash this message

    return render(request, 'contact.html')

    # return HttpResponse(" Contact us: 98xxxxxxx ")

def search(request):
    query = request.GET['query'].lower()
    list1 = ['umbrella', 'umbrellas', 'umbrella available', 'umbrellas available', ]
    list2 = ["1 fold umbrella", "1 fold umbrellas", "1 fold", "one fold", "one fold umbrellas", "one fold umbrella"]
    list3 = ["2 fold umbrella", "2 fold umbrellas", "2 fold", "two fold", "two fold umbrellas", "two fold umbrella"]
    list4 = ["3 fold umbrella", "3 fold umbrellas", "3 fold", "three fold", "three fold umbrellas", "three fold umbrella"]
    list5 = ["4 fold umbrella", "4 fold umbrellas", "4 fold", "four fold", "four fold umbrellas", "four fold umbrella"]
    list6 = ["5 fold umbrella", "5 fold umbrellas", "5 fold", "five fold", "five fold umbrellas", "five fold umbrella"]
    if query in list1:
        return render(request, 'search.html')

    elif query == "garden umbrella" or query == "garden umbrellas":
        return render(request, 'services2.html')

    elif query == "resort umbrella" or query == "resort umbrellas":
        return render(request, 'services3.html')

    elif query == "daily use umbrella" or query == "daily use umbrellas" or query == "umbrellas for daily use":
        return render(request, 'services1.html')

    elif query == "kids" or query == "kids umbrellas" or query == "kids umbrella":
        return render(request, 'kids.html' )

    elif query in list2:
        return render(request, '1_fold.html' )

    elif query in list3:
        return render(request, '2_fold.html' )

    elif query in list4:
        return render(request, '3_fold.html' )

    elif query in list5:
        return render(request, '4_fold.html' )

    elif query in list6:
        return render(request, '5_fold.html' )
    else:
        return render(request, 'error_page.html')
    # return HttpResponse("This is search tab.")
