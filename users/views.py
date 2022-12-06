
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def loginPage(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'registration/login.html')



def registerUser(request):

    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            user = authenticate(
                request, username=user.username, password=request.POST['password1']
            )

            if user is not None:
                login(request, user)
                return redirect('dashboard')

    context = {'form': form, 'page': page}
    return render(request, 'registration/register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('dashboard')