from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


def rating(request):
    context = {}
    return render(request, 'game_management/rating.html', context)
