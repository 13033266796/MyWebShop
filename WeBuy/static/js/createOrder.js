$(function () {
   $('.payment_btn').click(function () {
      var nickName = $('#islogin_1').text();
      var total_pay = $('.cart_price b').text();
      var goodsName = '';
      var goodsNumber = '';
      var pay = '';

      if($('.rememberMe:checked').size()==0){
          alert('请至少选择一件商品');
          return;
      }


      $('.rememberMe:checked:not(#checkall)').each(function () {
          goodsName += $(this).parent().next().find('.title_name').text()+',';
          goodsNumber += $(this).parent().next().next().next().find('input').val()+',';
          pay +=$(this).parent().next().next().next().next().text();
      });

      $.ajax({
          url:'/createOrder/',
          data:{
              nickName:nickName,
              total_pay:total_pay,
              goodsName:goodsName,
              goodsNumber:goodsNumber,
              pay:pay,
          },
          type:'get',
          dataType:'text',
          success:function (msg) {
              alert('下单成功');
              window.location = '/order'+msg+'/'
          },
          error:function (msg) {
              alert('下单失败')
          },
      })


   });


});