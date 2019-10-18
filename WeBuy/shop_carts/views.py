from django.shortcuts import render
from shop_user import isLogin_shop
from .models import CartsInfo,CollectInfo
from shop_user.models import UserInfo
from shop_goods.models import GoodsInfo,GoodsType
from django.core.paginator import Paginator
from django.http.response import HttpResponse,JsonResponse


# Create your views here.
@isLogin_shop.isLogin
def shopping_cart(request,pagIndex,isLogin=0):
    if pagIndex=='':
        pagIndex='1'

    nickName = request.session['nickName']
    context ={'id':1,'isLogin':isLogin,'nickName':nickName}
    user_id = UserInfo.objects.get(user_nickname=nickName).id
    #获取用户购物车
    myCart = CartsInfo.objects.filter(user_name = user_id).order_by('-id')#[篮子1，篮子2，篮子3，....]
    #将购物车商品分页显示，每页10个
    paginator = Paginator(myCart,10)
    page = paginator.page(int(pagIndex))

    if page.has_previous():
        pre_page = int(pagIndex)-1
    else:
        pre_page = int(pagIndex)
    if page.has_next():
        next_page = int(pagIndex)+1
    else:
        next_page = int(pagIndex)

    context.update({'page':page,'pre_page':pre_page,'next_page':next_page})
    return render(request,'shop_carts/shopping_cart.html',context)

#商品添加购物车
def addToCart(request,isLogin=0):
    productName = request.GET['product']
    nickName = request.GET['nickName']
    if request.GET.get('number'):
        number = int(request.GET.get('number'))
        print(number)
    else:
        number = 1

    product = GoodsInfo.objects.get(goods_name=productName)
    user = UserInfo.objects.get(user_nickname=nickName)

    #如果购物车中一存在同样商品 商品数量+1
    cart = CartsInfo.objects.filter(user_name=user).filter(goods_name=product)
    if len(cart)>=1:
        cart = cart[0]
        cart.productsNumber = cart.productsNumber+number
    else:
        cart = CartsInfo()
        cart.user_name=user
        cart.goods_name = product
        cart.productsNumber = number
    cart.save()
    return HttpResponse('1')

#获取用户购物车内商品数
def head_getCartsNumber(request):
    nickName = request.session['nickName']
    userId = UserInfo.objects.get(user_nickname=nickName).id
    number = len(CartsInfo.objects.filter(user_name = userId))
    return JsonResponse({'number':number})

#删除购物车内商品
def deleteGoods(request):
    nickName = request.GET['nickName']
    userId = UserInfo.objects.get(user_nickname=nickName).id
    product = request.GET['product']
    goodsId = GoodsInfo.objects.get(goods_name=product).id

    cart = CartsInfo.objects.get(user_name=userId,goods_name=goodsId)
    cart.delete()

    return HttpResponse('删除成功')

#批量删除购物车商品
def deleteAllGoods(request):
    nickName = request.GET['nickName']
    userId = UserInfo.objects.get(user_nickname=nickName).id
    product_list = request.GET['product_list'].split(',')
    products =[]
    for item in product_list:
        if item != '':
            products.append(item)
    carts = CartsInfo.objects.filter(user_name=userId)

    for item in carts:
        if item.goods_name.goods_name in products:
            item.delete()

    return HttpResponse('删除成功')

#商品点击收藏
def collectGoods(request):
    nickName = request.GET['nickName']
    product = request.GET['product']

    userId = UserInfo.objects.get(user_nickname=nickName)
    productId = GoodsInfo.objects.get(goods_name=product)

    try:
        if CollectInfo.objects.filter(user_name=userId,goods_name=productId):
            collect = CollectInfo.objects.get(user_name=userId,goods_name=productId)
            collect.delete()
            return JsonResponse({
                "result":True,
                "data":"Cancel"
            })
        else:
            collect = CollectInfo()
            collect.goods_name = productId
            collect.user_name = userId
            collect.save()
        return JsonResponse({
            "result": True,
            "data": "Success"
        })
    except Exception as ex:
        return JsonResponse({
            "result": False,
            "data": '操作出现异常：' + str(ex)
        })


def ligt_collect(request):
    product = request.GET['product']
    nickName = request.session['nickName']
    userId = UserInfo.objects.get(user_nickname=nickName).id
    productId = GoodsInfo.objects.get(goods_name=product).id
    if CollectInfo.objects.filter(user_name=userId,goods_name=productId):
        return JsonResponse({
            "result": True,
            "data": "Success"
        })
    return JsonResponse({
        "result": True,
        "data": "Cancel"
    })

#取消收藏
def delete_collect(request):
    nickName = request.GET['nickName']
    product = request.GET['product']

    userId = UserInfo.objects.get(user_nickname=nickName).id
    productId = GoodsInfo.objects.get(goods_name=product).id

    CollectInfo.objects.get(user_name=userId,goods_name=productId).delete()

    return HttpResponse('success')