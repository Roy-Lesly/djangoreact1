from django.contrib import admin
from .models import *


admin.site.register([RadiTestType, RadiTestCategory]) # RadiDept


@admin.register(RadiDept)
class RadiDeptAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)