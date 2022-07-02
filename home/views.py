from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.forms import Form_contact, NewsLatterForm
from home.models import Contact, NewsLatter
from mahsulot.models import Main, Category, Mahsulot, FeaturedBrand, FromBlog, Sale, Belowfooter, Footermodel, Appstore, \
    Aboutmain, Team, Comment, EvaraCorp, InContact, OurBlog, CategoryBlog


def home(request):
    main = Main.objects.all()
    kategoriy = Category.objects.all()
    mahsulot = Mahsulot.objects.filter(status=True).order_by('?')
    featuredbrand = FeaturedBrand.objects.all()
    fromblog = FromBlog.objects.all()
    sale = Sale.objects.all()
    belowfooter = Belowfooter.objects.all()
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()


    context = {
        'main': main,
        'kategoriy': kategoriy,
        'mahsulot': mahsulot,
        'featuredbrand': featuredbrand,
        'fromblog': fromblog,
        'sale': sale,
        'belowfooter': belowfooter,
        'footermodel': footermodel,
        'appstore': appstore,


    }


    return render(request, 'index.html',context)



def about(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    aboutmain = Aboutmain.objects.all()
    team = Team.objects.all()
    comment = Comment.objects.all()
    evaracorp = EvaraCorp.objects.all()
    featuredbrand = FeaturedBrand.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'aboutmain': aboutmain,
        'team': team,
        'comment': comment,
        'evaracorp': evaracorp,
        'featuredbrand': featuredbrand,
    }
    return render(request,'about.html',context)

def shop(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    mahsulot = Mahsulot.objects.filter(status=True).order_by('?')
    kategoriy = Category.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'mahsulot': mahsulot,
        'kategoriy': kategoriy,
    }
    return render(request,'shop.html',context)

def right(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    mahsulot = Mahsulot.objects.filter(status=True).order_by('?')
    kategoriy = Category.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'mahsulot': mahsulot,
        'kategoriy': kategoriy,
    }
    return render(request, 'right.html',context)


def bloggrid(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    ourblog = OurBlog.objects.all()
    kategoriy = CategoryBlog.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'ourblog': ourblog,
        'kategoriy': kategoriy,
    }
    return render(request, 'bloggrid.html',context)

def bloglist(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    ourblog = OurBlog.objects.all()
    kategoriy = CategoryBlog.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'ourblog': ourblog,
        'kategoriy': kategoriy,
    }
    return render(request,'bloglist.html',context)


def blogfull(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    ourblog = OurBlog.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'ourblog': ourblog,
    }
    return render(request, 'blogfull.html', context)

def pagecontact(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
    }
    return render(request,'pagecontact.html',context)

def pageaccount(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
    }
    return render(request,'pageaccount.html',context)

def loginregister(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
    }
    return render(request, 'pageloginregister.html', context)

def pagepurchase(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    ourblog = OurBlog.objects.all()
    kategoriy = CategoryBlog.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
        'ourblog': ourblog,
        'kategoriy': kategoriy,
    }
    return render(request,'pagepurchaseguide.html',context)

def page404(request):
    return render(request,'page404.html')

def shopwishlist(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
    }
    return render(request,'shopwishlist.html',context)

def shopcart(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
    }
    return render(request,'shopcart.html',context)


def compare(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    context = {
        'footermodel': footermodel,
        'appstore': appstore,
    }
    return render(request,'compare.html',context)



def contact(request):
    footermodel = Footermodel.objects.all()
    appstore = Appstore.objects.all()
    incontact = InContact.objects.all()
    if request.method == 'POST':
        form = Form_contact(request.POST)
        if form.is_valid():
            data = Contact()
            data.first_name = form.cleaned_data.get('first_name')
            data.email = form.cleaned_data.get('email')
            data.phone = form.cleaned_data.get('phone')
            data.subject = form.cleaned_data.get('subject')
            data.message = form.cleaned_data.get('message')
            data.save()
            return redirect('home')
    form = Form_contact
    context = {
        'form': form,
        'footermodel': footermodel,
        'appstore': appstore,
        'incontact': incontact,
    }
    return render(request,'pagecontact.html',context)


def newslatter(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = NewsLatterForm(request.POST)
        if form.is_valid():
            data = NewsLatter()
            data.email = form.cleaned_data['email']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Sizning emailingiz qabul qilindi')
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)
