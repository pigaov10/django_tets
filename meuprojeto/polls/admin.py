# -*- coding: utf-8 -*-
from django.contrib import admin
from meuprojeto.polls.models import Customer, Category


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
