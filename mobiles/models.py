from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


import uuid

class apple(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="apple")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200,  null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Apple', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class asus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="asus")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Asus', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class google(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="google")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Google', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class huawei(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="huawei")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Huawei', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class honor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="honor")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Honor', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class lenovo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="lenovo")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Lenovo', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class lg(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="lg")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Lg', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class motorola(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="motorola")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Motorola', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class nokia(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="nokia")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Nokia', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class oneplus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="oneplus")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Oneplus', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class oppo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="oppo")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Oppo', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class realme(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="realme")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Realme', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class redmi(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="redmi")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Redmi', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class samsung(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="samsung")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Samsung', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class sony(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="sony")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Sony', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class vivo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="vivo")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Vivo', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


class xiaomi(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True)
    Brand = models.CharField(max_length=100, default="xiaomi")
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='Xiaomi', default=None, null=True)
    date = models.DateField(null=True)

    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)

    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)

    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)

    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)

    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    more = RichTextUploadingField(null=True)

    def __str__(self):
        return self.Name


# comments 



class apple_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class asus_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class google_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class huawei_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class honor_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class lenovo_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class lg_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class motorola_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class nokia_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + self.user_id


class oneplus_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class oppo_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class realme_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class redmi_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class samsung_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class sony_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class vivo_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id


class xiaomi_comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    post_id = models.CharField(max_length=10000)
    user_id = models.CharField(max_length=10000)
    display_name = models.CharField(max_length=10000)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_id + " by " +  self.user_id






#for top 5b a   


class top_gaming(models.Model):
    Device_name = models.CharField(max_length=1000)
    Url = models.CharField(max_length=1000)    
    Performance_Os = models.CharField(max_length=100)
    Performance_Chipset = models.CharField(max_length=1000)
    Performance_GPU = models.CharField(max_length=1000)
    Performance_Ram = models.CharField(max_length=1000)
    Performance_Rom = models.CharField(max_length=1000)
    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)
    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)

    def __str__(self):
        return self.Device_name


class top_camera(models.Model):
    Device_name = models.CharField(max_length=1000)
    Url = models.CharField(max_length=1000)    
    Camera_Main = models.CharField(max_length=1000)
    Camera_Main_Video = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)
    Camera_Selfie_Video = models.CharField(max_length=1000)
    Camera_xtra = models.CharField(max_length=1000)
    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)

    def __str__(self):
        return self.Device_name

class top_office(models.Model):
    Device_name = models.CharField(max_length=1000)
    Url = models.CharField(max_length=1000)    
    Battery_Capacity = models.CharField(max_length=1000)
    Battery_Charging_Speed = models.CharField(max_length=1000)
    Display_Screen_Size = models.CharField(max_length=1000)
    Display_Resolution = models.CharField(max_length=1000)
    Display_Type = models.CharField(max_length=1000)
    Display_Pixels_Per_Inch = models.CharField(max_length=1000)
    Design_Dimensions = models.CharField(max_length=1000)
    Design_Weight = models.CharField(max_length=1000)
    Design_Colours = models.CharField(max_length=1000)
    Camera_Main = models.CharField(max_length=1000)
    Camera_Selfie = models.CharField(max_length=1000)

    def __str__(self):
        return self.Device_name