from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from adminpanel.forms import Forma
from adminpanel.models import Client, Creater


def register(request):
    if request.method == "POST":
        form = Forma(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            current_user = request.user
            data = Client()
            data.user_id = current_user.id
            data.save()
            return redirect('home')
        else:
            return redirect('register')

    form = Forma()
    context = {
        'form': form,
    }
    return render(request, 'pageloginregister.html', context)


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                Creater.objects.get(user_id=request.user.id)
                return redirect('creator')
            except:
                try:
                    Client.objects.get(user_id=request.user.id)
                    return redirect('pageaccount')
                except:
                    return redirect('login_form')
    else:
        return redirect('login_form')
    return render(request, 'pageloginregister.html')
