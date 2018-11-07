from django.shortcuts import render
from carapp.models import User
from django.http import HttpResponse
import os
from django.conf import settings
from django.core.paginator import Paginator
from carapp.models import *
# Create your views here.
import json
static=settings.STATICFILES_DIRS[0]
def login(request):
    cookie=request.COOKIES
    username=cookie.get("CARusername")
    password=cookie.get("CARpassword")
    if username!=None and password!=None:
        return render(request,"index.html",{"username":username})
    else:
        return render(request,'login.html')

def zhuce(request):

    return render(request,'zhuce.html')


def check(self):
    name = []
    namelist = User.usu.all()
    for user in namelist:
        name.append(user.username)
    return name



def tz(request):
    username1=request.POST.get("username")
    password1=request.POST.get("password")
    name = check(request)
    if username1 in name:
        word = User.usu.get(username=username1)
        word1 = word.password
        if password1==word1:
            res = render(request,"index.html",{"username":username1})
            res.set_cookie("CARusername", username1, max_age=6000)
            res.set_cookie("CARpassword", password1, max_age=6000)
            return res
        else:
            tishi = ["密码错误！请重新登录"]
            return render(request, "login.html", {"tishi": tishi})
    else:
        return render(request,"zhuce.html")




def update(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    tel=request.POST.get("num")
    name = User.usu.check()
    if username in name:
        return HttpResponse("用户已存在")
    else:
        User(username=username, password=password, tel=tel).save()

        return render(request, "login.html")




def index(request):
    cookie = request.COOKIES
    username = cookie.get("CARusername", "登录")
    return render(request,"index.html",{"username":username})


def buycar(request,pagenum,carlei):
    photolist = []
    cookie = request.COOKIES
    username = cookie.get("CARusername", "登录")
    usercarname=cookie.get("CARusername")
    # usercar文件夹的列表

    userlist = []

    if carlei == "0":
        userlist = os.listdir(os.path.join(os.path.join(static, 'image'), 'usercar'))
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})



    elif carlei == "1":
        name = "大众"
        indexlist=[]
        carobject = cardetail.car.filter(pingpai=name) #返回的是一个品牌名为奔驰的对象列表


        for user in carobject:
            userlist.append(user.chezhu)

        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "2":
        name = "别克"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "3":
        name = "本田"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "4":
        name = "标致"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "5":
        name = "雪佛兰"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "6":
        name = "宝马"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "7":
        name = "福特"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "8":
        name = "日产"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "9":
        name = "奥迪"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "10":
        name = "奔驰"
        carobject = cardetail.car.filter(pingpai=name) #返回的是一个品牌名为奔驰的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "11":
        name = "哈弗"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "12":
        name = "东风风神"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "13":
        name = "雪铁龙"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})
    elif carlei == "14":
        name = "现代"
        carobject = cardetail.car.filter(pingpai=name)  # 返回的是一个品牌名的对象列表
        for user in carobject:
            userlist.append(user.chezhu)
        for usernameimage in userlist:
            if usernameimage != None:
                img = os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage))[0]
                photolist.append(
                    os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), usernameimage),
                                 img))

        pi = Paginator(photolist, 5)
        pnums = pi.num_pages
        page = pi.page(pagenum)
        pnum = page.number
        sslist = page.object_list
        print(sslist)

        return render(request, "buycar.html", {"username": username, "sslist": sslist, "pnum": pnum, "pnums": pnums})


def salecar(request):
    cookie = request.COOKIES
    username = cookie.get("CARusername", "登录")
    return render(request,"salecar.html",{"username":username})


def tijiaocar(request):
    cookie = request.COOKIES
    username = cookie.get("CARusername", "登录")
    return render(request,"tijiaocar.html",{"username":username})

def upload(request):
    cookie = request.COOKIES
    username = cookie.get("CARusername")
    usernameimage = os.listdir(os.path.join(os.path.join(static, 'image'), 'usercar'))
    if username not in usernameimage:
        os.makedirs(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'),username))



    pingpai = request.POST.get("pingpai")
    chexi = request.POST.get("chexi")
    chexin = request.POST.get("chexin")
    licheng = request.POST.get("licheng")
    pailiang = request.POST.get("pailiang")
    biansuxiang = request.POST.get("biansuxiang")
    spsj = request.POST.get("spsj")
    spd = request.POST.get("spd")
    price = request.POST.get("price")
    zws = request.POST.get("zws")
    rylx = request.POST.get("rylx")
    chezhu = request.POST.get("chezhu")


    f = request.FILES['qctp']  # 从页面中获取照片文件
    path = os.path.join(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'), username),
                        str(f))  # 将它获取的照片文件存入到拼接的路径中
    f2 = open(path, "wb")
    f2.write(f.read())
    f2.close()

    mess=cardetail.car.insert(pingpai,chexi,chexin,licheng,pailiang,biansuxiang,spsj,spd,price,zws,rylx,chezhu)

    return HttpResponse(mess)

def cardetail2(request,count):
    cookie = request.COOKIES
    username = cookie.get("CARusername", "登录")
    usercarlist = os.listdir(os.path.join(os.path.join(static, 'image'), 'usercar'))
    user=usercarlist[int(count)]
    imgadress=os.listdir(os.path.join(os.path.join(os.path.join(static, 'image'), 'usercar'),user))[0]
    cz=cardetail.car.get(chezhu=user)
    pingpai=cz.pingpai
    chexin=cz.chexin
    chexi=cz.chexi
    price=cz.price
    pailiang=cz.pailiang
    licheng=cz.licheng
    biansuxiang=cz.biansuxiang
    spsj = cz.spsj
    spd = cz.spd
    zws = cz.zws
    rylx = cz.rylx
    id=cz.id
    return render(request,"cardetail.html",{"username":username,"pingpai":pingpai,"chexi":chexi,"chexin":chexin,"licheng":licheng,"pailiang":pailiang,"biansuxiang":biansuxiang,"spsj":spsj,"spd":spd,"price":price,"zws":zws,"rylx":rylx,"user":user,"imgadress":imgadress,"id":id})

def pay(request):
    cookie = request.COOKIES
    username = cookie.get("CARusername", "登录")
    return render(request,"paycar.html",{"username":username})

def gujia(request):
    return render(request,"gujia.html")

def buyer(request):
    json_receive = json.loads(request.body)
    tel = json_receive['tel']
    buycaruser.btel.charu(tel)
    return HttpResponse("预约成功")


