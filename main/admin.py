from django.contrib import admin
from .models import Serviceprovider,Postmsg,Search,occupations,numberofserviceproviders
# Register your models here.

admin.site.register(Serviceprovider)
admin.site.register(Postmsg)
admin.site.register(Search)
admin.site.register(occupations)
admin.site.register(numberofserviceproviders)

