# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrados
from .forms import RegModelForm

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["__unicode__","nombre","fecha"]
    form = RegModelForm
    list_filter = ["fecha"]
    list_editable = ["nombre"]
    search_fields = ["email", "nombre"]
    # class Meta: 
    #     model = Registrados


admin.site.register(Registrados, AdminRegistrado)


