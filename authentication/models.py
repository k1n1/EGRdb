from django.db import models


class signUpCode(models.Model):
    Email = models.EmailField()
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.Email


class passwordResetCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.email
