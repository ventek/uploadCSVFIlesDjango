from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def profile(request):
    return render(request, 'profile.html', {})


def about(request):
    return render(request, 'about.html', {})

