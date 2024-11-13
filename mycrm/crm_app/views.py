from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    #showing all the record on my home page
    records = Record.objects.all()

    #check to see if logging in 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            messages.success(request, "Ohh yeah!! You Have Been Logged In Successfully Welcome Back.")
            return redirect('home')
        else:
            messages.success(request, "Opps!! There Was An Error Logging In, Please Try Again..")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})



def logout_user(request):
    logout(request)
    messages.success(request, "Ohh No!! You Have Been Logged Out..")
    return redirect('home')
    



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    #only logged in user can view the details
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {' customer_record': customer_record})
    #if they are not logged in 
    else:
        messages.success(request, "You Have To Login To View That Page.")
        return redirect('home')

    
#creating a delete view 
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get()
        delete_it.delete()
        messages.success(request, "Record deleted Successfully.")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To Delete The Record...")
        return redirect('home')


#adding a new record
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Ohh Yeah!! Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})

    else:
        messages.success(request, "Opps!! You Must Login First...")
        return redirect('home')




    