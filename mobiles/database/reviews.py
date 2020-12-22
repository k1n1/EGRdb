from pymongo import MongoClient

con = MongoClient('localhost', 27017)


database = con.reviewsbybrand

tables_name = {
    "apple" : database.apple,
    "asus" : database.asus,
    "google" : database.google,
    "huawei" : database.huawei,
    "honor" : database.honor,
    "lenovo" : database.lenovo,
    "lg" : database.lg,
    "motorola" : database.motorola,
    "nokia" : database.nokia,
    "oneplus" : database.oneplus,
    "oppo": database.oppo,
    "realme" : database.realme,
    "redmi" : database.redmi,
    "samsung" : database.samsung,
    "sony" : database.sony,
    "vivo" : database.vivo,
    "xiaomi" : database.xiaomi,
}


def mobiles_reviews(user_id,mobile_id, mobile_name, display, design, camera, performance, battery):
    try:
        name = mobile_id.split("-")[0]
        for i in tables_name:
            if i == name:
                tables_name[i].insert_one({
                    "user_id":user_id,
                    "mobile_id" : mobile_id,
                    "mobile_name" : mobile_name,
                    "display" : int(display),
                    "design" : int(design),
                    "camera" : int(camera),
                    "performance" :int(performance),
                    "battery" : int(battery)
                    })
    except:
        print("somthing WRONG")


def mobiles_reviews_update(user_id,mobile_id, mobile_name, display, design, camera, performance, battery):
    try:
        name = mobile_id.split("-")[0]
        for i in tables_name:
            if i == name:
                tables_name[i].update_one({"user_id" : user_id, 'mobile_id' : mobile_id}, {
                    "$set" : {
                    "display" : int(display),
                    "design" : int(design),
                    "camera" : int(camera),
                    "performance" :int(performance),
                    "battery" : int(battery)
                    }
                    
                })
    except:
        print("somrthing WRONG")
