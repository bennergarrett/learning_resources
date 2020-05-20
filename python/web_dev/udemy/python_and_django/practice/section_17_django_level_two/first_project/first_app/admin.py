from django.contrib import admin
##telll model exists
##
from first_app.models import AccessRecord, Topic, Webpage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)

##create super user to implement
##