from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method=='POST':
        # print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            #   Create the User using form method
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()

            #Create the User using create_user method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            messages.error(request,'Your Account has been registered succesfully')
            return redirect('registerUser')
        else:
            print("invalid Form")
            print(form.errors)
    else:
        form= UserForm()
    context= {
        'form':form,
    }
    return render(request, 'accounts/registerUser.html',context)
