from django.contrib import admin

# Register your models here.
from core.models import contact,blogmodel,newsmodel
admin.site.register(contact)
admin.site.register(blogmodel)
admin.site.register(newsmodel)
# admin.site.register(datamod)
