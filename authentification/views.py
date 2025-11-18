from django.shortcuts import render, redirect
from .forms import CreateAccountForm, LoginForm
from .models import Account

# Create your views here.

def create_account_view(request):

    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            
            new_account = Account.objects.create(
                fullname=form.cleaned_data["fullname"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )


            request.session["logged_in_account_id"] = new_account.id

            return redirect('/posts')

    else:
        form = CreateAccountForm()

    return render(request, "create_account.html", {'form': form})



def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)

            try:
                account = Account.objects.get(email=email, password=password)
                request.session["logged_in_account_id"] = account.id
            except Account.DoesNotExist:
                print("Not exists")
                return redirect('/auth/login')
            

            return redirect('/posts')
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def logout_handler(request):
    request.session.flush()
    return redirect('/auth/login')
