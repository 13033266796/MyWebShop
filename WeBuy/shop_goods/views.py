#conding:utf-8
from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from .models import GoodsInfo,GoodsType
import json
from shop_user import isLogin_shop
from django.core.paginator import Paginator

#首页
def index(request,isLogin=0):
    if request.session.get('nickName'):
        isLogin = 1
        nickName = request.session['nickName']
        context ={'nickName':nickName,'isLogin':isLogin}
    else:
        context ={'isLogin':isLogin}

    #主页各分类最新商品
    newGoods1 = [GoodsInfo.objects.filter(goods_type=1).order_by('-id')[0].goods_name,
                GoodsInfo.objects.filter(goods_type=1).order_by('-id')[0].goods_price,
                GoodsInfo.objects.filter(goods_type=1).order_by('-id')[0].goods_originPlace,
                GoodsInfo.objects.filter(goods_type=1).order_by('-id')[0].goods_image,
                 GoodsInfo.objects.filter(goods_type=1).order_by('-id')[0].id,]

    newGoods2 = [GoodsInfo.objects.filter(goods_type=2).order_by('-id')[0].goods_name,
                GoodsInfo.objects.filter(goods_type=2).order_by('-id')[0].goods_price,
                GoodsInfo.objects.filter(goods_type=2).order_by('-id')[0].goods_originPlace,
                GoodsInfo.objects.filter(goods_type=2).order_by('-id')[0].goods_image,
                 GoodsInfo.objects.filter(goods_type=2).order_by('-id')[0].id,]

    newGoods3 = [GoodsInfo.objects.filter(goods_type=3).order_by('-id')[0].goods_name,
                GoodsInfo.objects.filter(goods_type=3).order_by('-id')[0].goods_price,
                GoodsInfo.objects.filter(goods_type=3).order_by('-id')[0].goods_originPlace,
                 GoodsInfo.objects.filter(goods_type=3).order_by('-id')[0].goods_image,
                 GoodsInfo.objects.filter(goods_type=3).order_by('-id')[0].id,]

    newGoods4 = [GoodsInfo.objects.filter(goods_type=4).order_by('-id')[0].goods_name,
                GoodsInfo.objects.filter(goods_type=4).order_by('-id')[0].goods_price,
                GoodsInfo.objects.filter(goods_type=4).order_by('-id')[0].goods_originPlace,
                GoodsInfo.objects.filter(goods_type=4).order_by('-id')[0].goods_image,
                 GoodsInfo.objects.filter(goods_type=4).order_by('-id')[0].id,]
    context.update({'newGoods1':newGoods1,'newGoods2':newGoods2,'newGoods3':newGoods3,'newGoods4':newGoods4})

    #分类商品
    typeGoods1 =[]
    for item in range(3):
        typeGoods1 .append([GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item+1].goods_image,
                            GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item+1].goods_price,
                            GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item+1].id,])

    typeGoods2 = []
    for item in range(3):
        typeGoods2.append([GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item + 1].goods_image,
                           GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item + 1].goods_price,
                           GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item+1].id,])

    typeGoods3 = []
    for item in range(3):
        typeGoods3.append([GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item + 1].goods_image,
                           GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item + 1].goods_price,
                           GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item+1].id,])

    typeGoods4 = []
    for item in range(3):
        typeGoods4.append([GoodsInfo.objects.filter(goods_type=4).order_by('-id')[item + 1].goods_image,
                           GoodsInfo.objects.filter(goods_type=4).order_by('-id')[item + 1].goods_price,
                           GoodsInfo.objects.filter(goods_type=4).order_by('-id')[item+1].id,])

    context.update({'typeGoods1':typeGoods1,'typeGoods2':typeGoods2,'typeGoods3':typeGoods3,'typeGoods4':typeGoods4})

    #推荐商品
    recommendGoods1 = [GoodsInfo.objects.filter(goods_type=1).order_by('id')[0].goods_name,
                       GoodsInfo.objects.filter(goods_type=1).order_by('id')[0].goods_price,
                       GoodsInfo.objects.filter(goods_type=1).order_by('id')[0].goods_image,
                       GoodsInfo.objects.filter(goods_type=1).order_by('id')[0].id,]

    recommendGoods2 = [GoodsInfo.objects.filter(goods_type=2).order_by('id')[0].goods_name,
                       GoodsInfo.objects.filter(goods_type=2).order_by('id')[0].goods_price,
                       GoodsInfo.objects.filter(goods_type=2).order_by('id')[0].goods_image,
                       GoodsInfo.objects.filter(goods_type=2).order_by('id')[0].id,]

    recommendGoods3 = [GoodsInfo.objects.filter(goods_type=3).order_by('id')[0].goods_name,
                       GoodsInfo.objects.filter(goods_type=3).order_by('id')[0].goods_price,
                       GoodsInfo.objects.filter(goods_type=3).order_by('id')[0].goods_image,
                       GoodsInfo.objects.filter(goods_type=3).order_by('id')[0].id,]

    recommendGoods4 = [GoodsInfo.objects.filter(goods_type=4).order_by('id')[0].goods_name,
                       GoodsInfo.objects.filter(goods_type=4).order_by('id')[0].goods_price,
                       GoodsInfo.objects.filter(goods_type=4).order_by('id')[0].goods_image,
                       GoodsInfo.objects.filter(goods_type=4).order_by('id')[0].id,]

    context.update({'recommendGoods1':recommendGoods1,'recommendGoods2':recommendGoods2,'recommendGoods3':recommendGoods3,'recommendGoods4':recommendGoods4})
    return render(request,'shop_goods/index.html',context)

#所有商品
def Products(request,isLogin=0):
    if request.session.get('nickName'):
        isLogin = 1
        nickName = request.session['nickName']
        context ={'nickName':nickName,'isLogin':isLogin}
    else:
        context ={'isLogin':isLogin}

    #各分类新上架的5个商品
    typeGoods1 = []
    for item in range(5):
        typeGoods1.append([GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item ].goods_image,
                           GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item ].goods_price,
                           GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item ].goods_name,
                           GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item ].goods_introduction,
                           GoodsInfo.objects.filter(goods_type=1).order_by('-id')[item ].id,])

    typeGoods2 = []
    for item in range(5):
        typeGoods2.append([GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item ].goods_image,
                           GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item ].goods_price,
                           GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item].goods_name,
                           GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item].goods_introduction ,
                           GoodsInfo.objects.filter(goods_type=2).order_by('-id')[item ].id,])

    typeGoods3 = []
    for item in range(5):
        typeGoods3.append([GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item ].goods_image,
                           GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item ].goods_price,
                           GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item].goods_name,
                           GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item].goods_introduction,
                           GoodsInfo.objects.filter(goods_type=3).order_by('-id')[item ].id,])

    context.update(
        {'typeGoods1': typeGoods1, 'typeGoods2': typeGoods2, 'typeGoods3': typeGoods3})

    return render(request,'shop_goods/Products.html',context)

#商品分类
def getGoodsType(request,typeId,pageIndex='1',isLogin=0):
    if request.session.get('nickName'):
        isLogin = 1
        nickName = request.session['nickName']
        context ={'nickName':nickName,'isLogin':isLogin}
    else:
        context ={'isLogin':isLogin}

    typeName = GoodsType.objects.get(pk=typeId).typeName

    tuijian = []
    for item in range(5):
        tuijian.append([
            GoodsInfo.objects.filter(goods_type=typeId).order_by('-goods_clickNumber')[item].goods_image,
            GoodsInfo.objects.filter(goods_type=typeId).order_by('-goods_clickNumber')[item].goods_name,
            GoodsInfo.objects.filter(goods_type=typeId).order_by('-goods_clickNumber')[item].goods_price,
            GoodsInfo.objects.filter(goods_type=typeId).order_by('-goods_clickNumber')[item].id,
        ])
    context.update({'tuijian':tuijian,'typeName':typeName,'typeId':typeId})

    #利用Paginator进行分页
    list = GoodsInfo.objects.filter(goods_type=typeId)
    myPaginator = Paginator(list,4)
    page = myPaginator.page(int(pageIndex))

    if page.has_next():
        next_page = int(pageIndex) + 1
    else:
        next_page = int(pageIndex)
    if page.has_previous():
        pre_page = int(pageIndex)-1
    else:
        pre_page = int(pageIndex)

    context.update({'page':page,'pre_page':pre_page,'next_page':next_page})
    return render(request,'shop_goods/ProductList.html',context)

def getGoods(request,id):
    goods_list = GoodsInfo.objects.filter(goods_type=id)
    list = []
    for item in goods_list:
        image = item.goods_image
        introduction = ''
        if len(item.goods_introduction)>15:
            for i in range(14):
                introduction += item.goods_introduction[i]
            introduction += '...'
        else:
            introduction = item.goods_introduction
        list.append([item.goods_name,str(image),item.goods_price,introduction])
    return JsonResponse({'data':list})

#商品详情
def Product(request,goodsId,isLogin=0):
    if request.session.get('nickName'):
        isLogin = 1
        nickName = request.session['nickName']
        context ={'nickName':nickName,'isLogin':isLogin}
    else:
        context ={'isLogin':isLogin}

    thisGoods = GoodsInfo.objects.get(pk=goodsId)

    goods_code = thisGoods.id
    goods_name = thisGoods.goods_name
    goods_image = thisGoods.goods_image
    goods_price = thisGoods.goods_price
    goods_unit = thisGoods.goods_unit
    goods_valueNumber = thisGoods.goods_valueNumber
    goods_introduction = thisGoods.goods_introduction
    goods_originPlace = thisGoods.goods_originPlace
    goods_content = thisGoods.goods_content
    goods_type = thisGoods.goods_type
    typeId = GoodsType.objects.get(typeName=goods_type).id
    context.update({'goods_code':goods_code,'goods_name':goods_name,'goods_image':goods_image,
                    'goods_price':goods_price,'goods_unit':goods_unit,'goods_valueNumber':goods_valueNumber,
                    'goods_introduction':goods_introduction,'goods_content':goods_content,'goods_type':goods_type,
                    'goods_originPlace':goods_originPlace,'typeId':typeId})

    #左侧推荐商品
    tuijian = []
    for item in range(5):
        tuijian.append([
            GoodsInfo.objects.all().order_by('-goods_clickNumber')[item].goods_image,
            GoodsInfo.objects.all().order_by('-goods_clickNumber')[item].goods_name,
            GoodsInfo.objects.all().order_by('-goods_clickNumber')[item].goods_price,
        ])
    context.update({
        'tuijian':tuijian
    })

    return render(request,'shop_goods/Product-detailed.html',context)

def clickNumber(request):
    goodsname = request.GET['name']

    goods = GoodsInfo.objects.get(goods_name=goodsname)
    goods.goods_clickNumber = int(goods.goods_clickNumber)+1
    goods.save()
    return JsonResponse({'data':'success'})