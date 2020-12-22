from django.shortcuts import render, HttpResponse, redirect
from .models import *
from news.models import news
from .database import reviews
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from pymongo import MongoClient

# con = MongoClient('localhost', 27017)
con = MongoClient('mongodb+srv://kini:7tdtu7CzFfiD0flR@egrdb-jslop.mongodb.net/egrdb?retryWrites=true&w=majority')

# for reviews by user
database = con.website
table = database.reviews


# for reviews by brands
database_brand = con.reviewsbybrand


brand_name = {
    "apple": apple,
    "asus": asus,
    "google": google,
    "huawei": huawei,
    "honor": honor,
    "lenovo": lenovo,
    "lg": lg,
    "motorola": motorola,
    "nokia": nokia,
    "oneplus": oneplus,
    "oppo": oppo,
    "realme": realme,
    "redmi": redmi,
    "samsung": samsung,
    "sony": sony,
    "vivo": vivo,
    "xiaomi": xiaomi,
}
user_comments = {
    "apple": apple_comments,
    "asus": asus_comments,
    "google": google_comments,
    "huawei": huawei_comments,
    "honor": honor_comments,
    "lenovo": lenovo_comments,
    "lg": lg_comments,
    "motorola": motorola_comments,
    "nokia": nokia_comments,
    "oneplus": oneplus_comments,
    "oppo": oppo_comments,
    "realme": realme_comments,
    "redmi": redmi_comments,
    "samsung": samsung_comments,
    "sony": sony_comments,
    "vivo": vivo_comments,
    "xiaomi": xiaomi_comments,
}


# for find average total

tables_name = {
    "apple": database_brand.apple,
    "asus": database_brand.asus,
    "google": database_brand.google,
    "huawei": database_brand.huawei,
    "honor": database_brand.honor,
    "lenovo": database_brand.lenovo,
    "lg": database_brand.lg,
    "motorola": database_brand.motorola,
    "nokia": database_brand.nokia,
    "oneplus": database_brand.oneplus,
    "oppo": database_brand.oppo,
    "realme": database_brand.realme,
    "redmi": database_brand.redmi,
    "samsung": database_brand.samsung,
    "sony": database_brand.sony,
    "vivo": database_brand.vivo,
    "xiaomi": database_brand.xiaomi,
}


def index(request):
    if request.method == 'GET':
        all_news = news.objects.all().order_by('-date')
        page_per_items = Paginator(all_news, 4)
        page = request.GET.get("page")
        all_news = page_per_items.get_page(page)

        return render(request, './index.html', {"all_news": all_news})
    else:
        return render(request, './error/404.html')


def mobiles(request):
    if request.method == 'GET':
        return render(request, './mobiles.html')
    else:
        return render(request, './error/404.html')


def brand(request, brand):
    if request.method == 'GET':
        device = None
        for i in brand_name:
            if i == brand:
                device = brand_name[i].objects.all().order_by("-date")
                return render(request, './brand.html', {'brand': device, 'title': brand.capitalize()})
                break
        else:
            return render(request, './error/404.html')
    else:
        return render(request, './error/404.html')


def full(request, url):
    if request.method == 'GET':
        total_count = None
        total_display = None
        total_design = None
        total_camera = None
        total_performance = None
        total_battery = None
        name = url.split("-")[0]
        for i in tables_name:
            if i == name:

                # need to optimaize
                a = tables_name[i].aggregate([
                    {"$match": {
                        "mobile_id": url
                    }
                    },
                    {"$group": {"_id": "$mobile_id", "count": {"$sum": 1}, "display": {"$avg": "$display"}, "design": {
                        "$avg": "$design"}, "camera": {"$avg": "$camera"}, "performance": {"$avg": "$performance"}, "battery": {"$avg": "$battery"}}
                     }
                ])
                for j in a:
                    total_count = j['count']
                    total_display = float(str(j['display'])[:4])
                    total_design = float(str(j['design'])[:4])
                    total_camera = float(str(j['camera'])[:4])
                    total_performance = float(str(j['performance'])[:4])
                    total_battery = float(str(j['battery'])[:4])
        device = None
        req_brand = url.split("-")
        id = str(request.user)
        try:
            user_reviews = table.find_one({'user_id': id})
            for i in (user_reviews['mobiles']):
                for k in i:
                    a = k
                    if a == url:
                        display = i[k]['display']
                        design = i[k]['design']
                        camera = i[k]['camera']
                        performance = i[k]['performance']
                        battery = i[k]['battery']
        except:
            pass
        template = 'full.html'
        try:
            device = None
            all_comments = None
            for i in brand_name:
                if i == req_brand[0]:
                    device = brand_name[i].objects.filter(url=url).first()
                    more = brand_name[i].objects.all().order_by('?')[:6]
                    all_comments = user_comments[i].objects.filter(post_id=url)
                    if device:
                        break

            else:
                template = '404.html'
            try:
                return render(request, template, {
                    'device': device,
                    'id': id,
                    'display': display,
                    'design': design,
                    'camera': camera,
                    'performance': performance,
                    'battery': battery,
                    'review': 'done',
                    'total_count': total_count,
                    'total_display': total_display,
                    'total_design': total_design,
                    'total_camera': total_camera,
                    'total_performance': total_performance,
                    'total_battery': total_battery,
                    'all_comments': all_comments,
                    'more': more,
                })
            except:
                return render(request, template, {
                    'device': device,
                    'id': id,
                    'total_count': total_count,
                    'total_display': total_display,
                    'total_design': total_design,
                    'total_camera': total_camera,
                    'total_performance': total_performance,
                    'total_battery': total_battery,
                    'all_comments': all_comments,
                    'more': more
                })

        except:
            return render(request, template)
    else:
        return render(request, './error/404.html')


def comments(request):
    if request.method == 'POST':
        user = str(request.POST['user'])
        mobile_id = str(request.POST['mobile_id'])
        display_name = str(request.POST['display_name'])
        comment = str(request.POST['comment'])
        url = mobile_id.split("-")
        for i in user_comments:
            if i == url[0]:
                user_comments[i](user_id=user, post_id=mobile_id,
                                 display_name=display_name, comments=comment).save()
        return HttpResponse("comment send")
    else:
        return render(request, './error/404.html')


def commentsdelete(request):
    if request.method == 'POST':
        mobile_id = request.POST['mobile_id']
        user = request.POST['user']
        id = request.POST['id']
        url = mobile_id.split("-")
        for i in user_comments:
            if i == url[0]:
                if request.user.username == user:
                    user_comments[i].objects.filter(id=id).first().delete()
                    return HttpResponse("Your comment id Remove")
                else:
                    return HttpResponse(id)
    else:
        return render(request, './error/404.html')


# REVIEWS


def new_reviews(request):
    if request.method == 'POST':
        database = con.website
        table = database.reviews
        user_id = str(request.POST['user'])
        mobile_id = str(request.POST['mobile_id'])
        mobile_name = str(request.POST['mobile_name'])
        display = str(request.POST['display'])
        design = str(request.POST['design'])
        camera = str(request.POST['camera'])
        performance = str(request.POST['performance'])
        battery = str(request.POST['battery'])
        reviews.mobiles_reviews(
            user_id, mobile_id, mobile_name, display, design, camera, performance, battery)
        if table.find_one({'user_id': user_id}):
            table.update_one(
                {'user_id': user_id},
                {"$push": {

                    "mobiles":
                        {

                            mobile_id: {
                                "name": mobile_name,
                                "display": int(display),
                                "design": int(design),
                                "camera": int(camera),
                                "performance": int(performance),
                                "battery": int(battery)

                            },

                        }

                }

                },
            )

        else:
            table.insert_one({
                'user_id': user_id,
                'mobiles': [{

                    mobile_id: {
                        'name': mobile_name,
                        'display': int(display),
                        'design': int(design),
                        'camera': int(camera),
                        'performance': int(performance),
                        'battery': int(battery),

                    }

                }]
            })
        return HttpResponse("Your Reviews add in our database")

    else:
        return render(request, './error/404.html')


def update_reviews(request):
    if request.method == "POST":
        database = con.website
        table = database.reviews
        user_id = str(request.POST['user'])
        mobile_id = str(request.POST['mobile_id'])
        mobile_name = str(request.POST['mobile_name'])
        display = str(request.POST['display'])
        design = str(request.POST['design'])
        camera = str(request.POST['camera'])
        performance = str(request.POST['performance'])
        battery = str(request.POST['battery'])
        reviews.mobiles_reviews_update(
            user_id, mobile_id, mobile_name, display, design, camera, performance, battery)
        device_name = mobile_id
        update_str = str("mobiles." + device_name)
        table.update_one({"user_id": user_id, update_str: {"$exists": "true"}},
                         {
                             "$set": {
                                 "mobiles.$": {
                                     device_name: {
                                         "name": mobile_name,
                                         "display": int(display),
                                         "design": int(design),
                                         "camera": int(camera),
                                         "performance": int(performance),
                                         'battery': int(battery)

                                     }
                                 }
                             }
        })
        return HttpResponse("Your Reviews is update")
    else:
        return render(request, './error/404.html')
