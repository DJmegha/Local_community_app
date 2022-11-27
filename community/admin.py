from django.contrib import admin
from .models import Services,Categories,ServiceProviders, Comment
from django.contrib.auth.models import Group
from django.utils.html import format_html
    
# Register your models here.
admin.site.register(Services)
admin.site.register(Categories)
admin.site.register(ServiceProviders)
admin.site.register(Comment)





#to change the heading of admin
admin.site.site_header='Local community Admin panel'
admin.site.site_title='Local community  Admin Panel'

#unregister model
admin.site.unregister(Group)
