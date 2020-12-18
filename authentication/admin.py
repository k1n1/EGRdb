from django.contrib import admin

# Register your models here.
from .models import signUpCode, passwordResetCode

admin.site.register(signUpCode)
admin.site.register(passwordResetCode)