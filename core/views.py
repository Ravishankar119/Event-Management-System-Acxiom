from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LoginForm

def index(request):
    return render(request, 'core/index.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Simple role detection by staff flag and group (simplified)
            if user.is_staff:
                return redirect('admin_dashboard')
            # For this scaffold we treat username starting with 'vendor' as vendor
            if user.username.startswith('vendor'):
                return redirect('vendor_dashboard')
            return redirect('user_dashboard')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

@login_required
def vendor_dashboard(request):
    # in real app check vendor ownership
    return render(request, 'core/vendor_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'core/user_dashboard.html')
