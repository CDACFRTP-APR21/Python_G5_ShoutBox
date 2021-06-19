from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
# Register your models here.

from .models import Comments, Friends, ReportedShouts, Shouts, Users


admin.site.site_header = "Admin DashBoad"
admin.site.site_title = "ShoutBox"
admin.site.index_title = ''

class UserAdmin(admin.ModelAdmin):
    sortable_by = 'UserId'
    search_fields = ['UserName','FirstName','LastName','Email','IsActive']
    list_display = ('UserId','image_tag','UserName','FirstName','LastName','Email','MobileNo','Password','DateOfBirth','IsActive')
    list_display_links = ('UserName',)
    list_filter = ('IsActive',)
    list_editable = ('IsActive',)


admin.site.register(Users,UserAdmin)
admin.site.register(Shouts)
admin.site.register(Comments)
admin.site.register(Friends)
admin.site.register(ReportedShouts)
