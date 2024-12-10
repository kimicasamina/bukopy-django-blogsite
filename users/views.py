from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 

def register_view(request):
    if request.method == "POST":
        # validate form, save to the database and redirect to another url
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else: 
        # create an empty form instead and send the form errors
        form = UserCreationForm()
    return render(request, 'users/register.html', { "form": form })