from django.contrib import admin
from .models import Services, Portfolio, Team


# Register your models here.

# admin.site.register(Services)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}