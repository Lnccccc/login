from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .form import LoginForn

def user_login(request):
    if request.method == 'POST':
        form = LoginForn(request.POST):
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None :
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfuly')
                else:
                     return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForn()
        return render(request,'account/login.html',context={"form":form})
    
