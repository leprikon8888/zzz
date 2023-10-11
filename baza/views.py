from django.shortcuts import render
from .models import Services, Team


def main_page(request):
    services = Services.objects.filter(is_visible=True)
    teams = Team.objects.filter(is_visible=True)

    return render(request, 'main.html', context={'services': services, 'teams': teams})