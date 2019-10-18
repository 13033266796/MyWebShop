#conding:utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import UserInfo,AreaInfo
from hashlib import sha1
from django.conf import settings
import os
from . import isLogin_shop
from shop_carts.models import CollectInfo
from django.core.paginator import Paginator


# Create your views here.
def base(request):
    return render(request,'shop_user/base_head_foot.html')
#用户注册
def register(request):
    return render(request,'shop_user/registered.html')
def registerPost(request):
    userName = request.POST['userName'],
    pwd=request.POST['pwd'],
    code=request.POST['code']
    mobile=request.POST['mobile']
    if code != request.session['verifyCode']:
        return HttpResponse('0')#验证码有误

    s1 = sha1()
    s1.update(pwd[0].encode('utf-8'))
    newPwd = s1.hexdigest()
    print(newPwd)

    #验证是否已经注册过
    if  UserInfo.objects.filter(user_nickname=userName):
        return HttpResponse('2')#用户名存在
    elif UserInfo.objects.filter(user_number=mobile):
        return HttpResponse('3')#手机号已经注册过
    else:
        #创建对象
        user = UserInfo()
        user.user_nickname = userName[0]
        user.user_number = mobile
        user.user_pwd = newPwd
        user.save()
        return HttpResponse('1')#注册成功

#生成验证码
def verifyCode(request):
    #引入绘图模块,随机数模块
    from PIL import ImageDraw,ImageFont,Image
    import random

    #定义变量，用于图片的背景色，宽，高
    backGroundColor = ((random.randrange(20, 100), random.randrange(20, 100), 255))
    width = 100
    height = 25

    #创建图片对象
    codeImage = Image.new('RGB',(width,height),backGroundColor)

    #创建画笔对象
    draw = ImageDraw.Draw(codeImage)

    #调用画笔的point方法 绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy,fill)

    #定义验证码的备选项
    allStr = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选4个作为验证码
    code = ''
    for i in range(0,4):
        code += allStr[random.randrange(0,len(allStr))]
    #构造字体对象
    font = ImageFont.truetype('C:\Windows\Fonts\simfang.ttf', 23)
    #构造字体颜色
    fontColor = (255,255,255)
    #绘制四个字符
    for i in range(len(code)):
        draw.text((i*25,2),code[i],font=font,fill=fontColor)

    #存入session做进一步验证
    request.session['verifyCode'] = code
    #内存文件操作
    import io
    buf = io.BytesIO()
    #保存图片在内存中，文件类型png
    codeImage.save(buf,'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')
#核对验证码
def checkVerifyCode(request):
    # print(request.session['verifyCode'])
    if request.POST['code'] == request.session['verifyCode']:
        return HttpResponse('1') #正确
    else:
        return HttpResponse("2")#不正确

#用户登录
def Login(request):
    nickName = request.session.get('nickName','未登录')
    context ={'nickName':nickName}
    return render(request,'shop_user/Login.html',context)
def LoginPost(request):
    nickName = request.POST['nickName']
    Pwd = request.POST['Pwd']
    url = request.COOKIES.get('url','/index/')
    if url=='':
        url = '/index/'
    #密码加密
    s1 = sha1()
    s1.update(Pwd.encode('utf-8'))
    newPwd = s1.hexdigest()

    #判断用户是否注册
    if UserInfo.objects.filter(user_nickname=nickName):
        if UserInfo.objects.filter(user_nickname=nickName).values('user_pwd')[0]['user_pwd']==newPwd:
            request.session['nickName']=nickName
            context = {'isLogin':'1'}
            return HttpResponse(url)#登录成功
        else:
            return HttpResponse('1')#密码错误
    else:
        return HttpResponse('0')#用户不存在
#退出登录
def Logout(request):
    if request.session.get('nickName'):
        del request.session['nickName']

    red = HttpResponseRedirect('/Login/')
    red.set_cookie('url', '')
    return red



#个人中心
@isLogin_shop.isLogin
def user(request,isLogin):
    nickName = request.session['nickName']
    score = UserInfo.objects.filter(user_nickname=nickName).values('user_score')[0]['user_score']
    money = UserInfo.objects.filter(user_nickname=nickName).values('user_money')[0]['user_money']
    context = {'nickName':nickName,'score':score,'money':money,'isLogin':isLogin}
    return render(request,'shop_user/user.html',context)

@isLogin_shop.isLogin
def user_info(request,isLogin):
    nickName = request.session['nickName']
    number = UserInfo.objects.filter(user_nickname=nickName).values('user_number')[0]['user_number']
    realName = UserInfo.objects.filter(user_nickname=nickName).values('user_name')[0]['user_name']
    gender = UserInfo.objects.filter(user_nickname=nickName).values('user_gender')[0]['user_gender']
    mail = UserInfo.objects.filter(user_nickname=nickName).values('user_mail')[0]['user_mail']
    context = {'nickName':nickName,'number':number,'gender':gender,'realName':realName,'mail':mail,'isLogin':isLogin}
    return render(request,'shop_user/user_info.html',context)

def user_infoPost(request):
    nickName = request.POST['nickName']
    realName = request.POST['realName']
    gender =request.POST['gender'],
    number =request.POST['number'],
    mail = request.POST['mail'],
    print(gender)
    #查找对象
    user = UserInfo.objects.get(user_nickname=nickName)
    user.user_name = realName
    user.user_number = number[0]
    user.user_mail = mail[0]
    if gender[0]=='1':
        user.user_gender = True
    else:
        user.user_gender = False
    user.save()

    return  HttpResponse('1')

@isLogin_shop.isLogin
def user_Password(request,isLogin):
    nickName = request.session['nickName']
    context = {'nickName':nickName,'isLogin':isLogin}
    return render(request,'shop_user/user_Password.html',context)
#修改密码
def updatePwdPost(request):
    nickName = request.session['nickName']
    prePwd = request.POST['prePwd']
    newPwd = request.POST['newPwd']
    #密码加密
    s1 = sha1()
    s1.update(prePwd.encode('utf-8'))
    prePwd_s = s1.hexdigest()
    s2 = sha1()
    s2.update(newPwd.encode('utf-8'))
    newPwd_s = s2.hexdigest()

    #查找对象
    user = UserInfo.objects.get(user_nickname=nickName)
    if prePwd_s == user.user_pwd:
        user.user_pwd = newPwd_s
        user.save()
    else:
        return HttpResponse('prePwd_error')

    user.save()
    print(nickName,prePwd,newPwd)
    return HttpResponse('yes')
#换头像
# def updateHead(request):
#     return HttpResponse('yes')
def headPost(request):
    nickName = request.session['nickName']
    img = request.FILES['newHead']
    imgName = os.path.join(settings.MEDIA_ROOT,nickName+'.jpg')
    with open(imgName,'wb') as f:
        for content in img.chunks():
            f.write(content)
    print(nickName,img)
    return redirect('/user/')
def checkHead(request):
    img = request.GET['img']
    if os.path.exists(settings.BASE_DIR+img):
        return HttpResponse('1')

#收货地址
@isLogin_shop.isLogin
def user_address(request,isLogin):
    nickName = request.session['nickName']
    #查找对象
    user = UserInfo.objects.get(user_nickname=nickName)
    context ={'nickName':nickName,
              'realName':user.user_name,
              'number':user.user_number,
              'pro':user.user_address.split(',')[0],
              'city':user.user_address.split(',')[1],
              'dis':user.user_address.split(',')[2],
              'address':user.user_address.split(',')[3],
              'youbian':user.user_youbian,
              'telephone':user.user_telephone,
              'isLogin':isLogin}
    return render(request,'shop_user/user_address.html',context)
#获取省信息
def pro(request):
    pro_list = AreaInfo.objects.filter(parent_ad_code=100000)
    list = []
    for item in pro_list:
        list.append([item.ad_code,item.name])
    return JsonResponse({'data':list})
#获取市、区、县信息
def cityAndDis(request,id):
    cityAndDis_list = AreaInfo.objects.filter(parent_ad_code=int(id))
    list = []
    for item in cityAndDis_list:
        list.append({'id':item.ad_code,'name':item.name})
    return JsonResponse({'data':list})
def addressPost(request):
    nickName = request.session['nickName']
    realName = request.POST['realName']
    pro = request.POST['pro']
    city = request.POST['city']
    dis = request.POST['dis']
    detail_address = request.POST['detail_address']
    youbian = request.POST['youbian']
    number = request.POST['number']
    telephone = request.POST['telephone']
    print(detail_address,youbian,number,telephone)

    #查找对象
    user = UserInfo.objects.get(user_nickname=nickName)
    user.user_name = realName
    user.user_address = pro+','+city+','+dis+','+detail_address
    user.user_youbian = youbian
    user.user_number = number
    user.user_telephone = telephone
    user.save()
    return HttpResponse('添加成功')

@isLogin_shop.isLogin
def user_Collect(request,pageIndex,isLogin):
    nickName = request.session['nickName']
    context = {'nickName':nickName,'isLogin':isLogin}
    userId = UserInfo.objects.get(user_nickname=nickName).id
    if pageIndex=='':
        pageIndex = '1'
    #获取用户收藏的商品
    collect_goods_list =  CollectInfo.objects.filter(user_name=userId).order_by('-id')

    #将收藏的商品分页显示
    paginator = Paginator(collect_goods_list,7)
    page = paginator.page(int(pageIndex))

    if page.has_next():
        next_page = int(pageIndex) + 1
    else:
        next_page = int(pageIndex)

    if page.has_previous():
        pre_page = int(pageIndex) - 1
    else:
        pre_page = int(pageIndex)

    context.update({'page':page,'pre_page':pre_page,'next_page':next_page})

    return render(request,'shop_user/user_Collect.html',context)

@isLogin_shop.isLogin
def user_integral(request,isLogin):
    nickName = request.session['nickName']
    context = {'nickName':nickName,'isLogin':isLogin}
    return render(request,'shop_user/user_integral.html',context)