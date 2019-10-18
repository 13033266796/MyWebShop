from django.shortcuts import render,redirect
from django.http.response import HttpResponse,JsonResponse
import datetime
from .models import orderGoods,OrderInfo
from shop_user.models import UserInfo
from shop_goods.models import GoodsInfo
from shop_carts.models import CartsInfo

# Create your views here.
def order(request,orderCode):
    nickName = request.session.get('nickName','')
    if nickName=='':
        return redirect('/index/')

    order = OrderInfo.objects.get(pk=orderCode)
    # 用户信息及地址
    realName = order.user_name.user_name
    user_address = ''.join( order.user_name.user_address.split(',') )
    user_number = order.user_name.user_number
    user_mail = order.user_name.user_mail
    user_youbian = order.user_name.user_youbian
    user_telephone = order.user_name.user_telephone

    # print(realName,user_address,user_number,user_mail,user_youbian,user_telephone)
    context = {'realName':realName,'user_address':user_address,'user_number':user_number,
               'user_mail':user_mail,'user_youbian':user_youbian,'user_telephone':user_telephone,
               'orderCode':orderCode}

    total_pay = order.total_pay
    context.update({'total_pay':total_pay})

    return render(request,'shop_order/Orders.html',context)

def getOrderGoods(request,orderCode):
    order = OrderInfo.objects.get(pk=orderCode)
    myGoods = orderGoods.objects.filter(belong_order=order)  # 订单内所有商品列表

    show_goods = []
    for item in myGoods:
        # print(item.goods_name.goods_image)
        show_goods.append([str(item.goods_name.goods_image),     # 0 图片
                           item.goods_name.goods_name,      # 1 名称
                           item.goods_name.goods_price,     # 2 单价
                           item.count,                      # 3 购买数量
                           item.pay])                       # 4 小计


    return JsonResponse({'data':show_goods})


#生成订单
def createOrder(request):
    #获取数据
    nickName = request.GET['nickName']
    total_pay = request.GET['total_pay']
    goodsName = request.GET['goodsName']
    goodsNumber = request.GET['goodsNumber']
    pay = request.GET['pay']
    #格式化数据
    total_pay = float(total_pay.split('￥')[1])
    goodsName_list =goodsName.split(',')
    goodsNumber_list = goodsNumber.split(',')
    pay_list = pay.split('￥')
    goodsName_list.pop()
    goodsNumber_list.pop()
    pay_list.pop(0)

    #新建订单表和订单详表
    orderCode = ''#订单编号
    now = str(datetime.datetime.now()).split('.')[0]
    for i in range(len(now)):
        if now[i] not in [' ','-',':']:
            orderCode += now[i]
    print(orderCode) #订单编号
    #订单总表
    order = OrderInfo()
    order.order_code = orderCode
    order.user_name = UserInfo.objects.get(user_nickname = nickName)
    order.total_pay = total_pay
    order.user_address = UserInfo.objects.get(user_nickname = nickName).user_address
    order.save()
    #订单详表
    for i in range(len(goodsNumber_list)):
        ordergoods = orderGoods()
        ordergoods.goods_name = GoodsInfo.objects.get(goods_name = goodsName_list[i])
        ordergoods.belong_order = OrderInfo.objects.get(order_code = orderCode)
        ordergoods.pay = pay_list[i]
        ordergoods.count = goodsNumber_list[i]
        ordergoods.save()

    print(goodsName_list)
    print(goodsNumber_list)

    #下单成功 将购物车内相应商品删除
    #商品库存减去相应数量
    for i in range(len(goodsNumber_list)):
        CartsInfo.objects.get(user_name=UserInfo.objects.get(user_nickname=nickName),goods_name=GoodsInfo.objects.get(goods_name=goodsName_list[i])).delete()
        goods = GoodsInfo.objects.get(goods_name=goodsName_list[i])
        goods.goods_valueNumber = int(goods.goods_valueNumber) - int(goodsNumber_list[i])
        goods.save()
    return HttpResponse(orderCode)

def getMyOrder(request):
    nickName = request.session.get('nickName','')
    if nickName == '':
        return redirect('/Login/')


    new_order = OrderInfo.objects.filter(user_name=UserInfo.objects.get(user_nickname=nickName)).order_by('-order_time')[0]
    orderCode = new_order.order_code
    total_pay = new_order.total_pay

    goods_info = orderGoods.objects.filter(belong_order=new_order)
    # print(goods_info)
    list = []
    for item in goods_info:
        list.append([str(item.goods_name.goods_image),
                     item.goods_name.goods_name,
                     item.goods_name.goods_price,
                     item.count])

    return JsonResponse({'orderCode':orderCode,'data':list,'total_pay':total_pay})