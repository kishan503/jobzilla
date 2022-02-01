from django.contrib import admin
from .models import *


# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Company_Gallary)
admin.site.register(PostLike)
admin.site.register(CompanyFollower)
admin.site.register(JobPost)