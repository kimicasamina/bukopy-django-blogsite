from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register_view(request):
    print("REQUEST:", request)
    if request.method == "POST":
        # validate form, save to the database and redirect to another url
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())

            return redirect("posts:list")
    else: 
        # create an empty form instead and send the form errors
        form = UserCreationForm()
    return render(request, 'users/register.html', { "form": form })

def login_view(request):
    print("REQUEST:", request)
    if request.method == "POST":
        # validate form, redirect to another url
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print(form.get_user())
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else: 
        # create an empty form instead and send the form errors
        form = AuthenticationForm()
    return render(request, 'users/login.html', { "form": form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:login')