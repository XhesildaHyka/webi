from django.shortcuts import render
from .models import *

def home(request):
    categorys = Category.objects.all()
    items = Item.objects.all()
    arrivals = Arrival.objects.all()
    detailItem = Product.objects.all()
    context = {
        "categorys": categorys,
        "detailItem": detailItem,
        "items": items,
        "arrivals": arrivals,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):   
    if request.method == "POST":
       first_name= request.POST["emri"]
       last_name= request.POST["lastname"]
       email= request.POST["email"]
       message= request.POST["sms"]
       Contact(contact_name=first_name,contact_lastname=last_name,contact_email=email,contact_sms=message).save()
    return render(request, 'contact.html')

def details(request, id ):
    detailItem=Product.objects.get(pk=id)
    context={"detailItem": detailItem}
    return render(request, 'details.html',context)

def kategori(request, id):
    categorys=Category.objects.get(pk=id)
    items=Product.objects.filter(product_category=categorys)
    
    context={"categorys": categorys,"items": items,}
    return render(request, 'kategori.html',context)

def item(request, id):
    items=Item.objects.get(pk=id)
    ndarja=Product.objects.filter(product_item=items)
    context={"items": items,"ndarja": ndarja}
    return render(request, 'item.html',context)

def arrival(request, id):
    arrivals = Arrival.objects.get(pk=id)  
    reja = Product.objects.filter(product_arrival=arrivals)
    context = {"arrivals": arrivals, "reja": reja} 
    return render(request, 'arrival.html', context)



def search(request):
    if request.method == "GET":
        search = request.GET.get("search")
        if search:
            posts = Product.objects.filter(product_title__icontains=search)
        else:
            posts = Product.objects.all()  # Show all products if no search term
        return render(request, 'search.html', {"posts": posts})
