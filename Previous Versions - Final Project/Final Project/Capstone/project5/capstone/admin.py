from django.contrib import admin
from .models import User, Contact, Referral, Timeline

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Referral)
admin.site.register(Timeline)
