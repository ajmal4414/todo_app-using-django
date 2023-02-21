from django.contrib import admin
from .models import Tasks, Register, Login

# Register your models here.

admin.site.register(Tasks)
admin.site.register(Login)
admin.site.register(Register)