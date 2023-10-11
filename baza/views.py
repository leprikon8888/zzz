from django.shortcuts import render
from .models import Services


def main_page(request):
    services = Services.objects.filter(is_visible=True)

    return render(request, 'main.html', context={'services': services})