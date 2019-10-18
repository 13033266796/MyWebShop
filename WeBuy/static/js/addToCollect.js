$(function () {
    //列表页加入收藏
   $('.Collect').click(function () {
      var product = $(this).next().next().text();
      var nickName = $('#islogin_1').text();
      var love = $(this);
      $.get('/collectGoods/?product='+product+'&nickName='+nickName,function(msg){
          if(msg.result){
              if(msg.data == 'Cancel'){
                  love.css('background-position','right 0px');
              }
              else if(msg.data == 'Success'){
                  love.css('background-position','right -17px');
              }
          }
          else{
              alert(msg.data);
          }
      });
   });

    //详情页加入收藏
   $('.Collect_btn').click(function () {
      var product = $(this).parent().prev().prev().prev().prev().find('h2').text();
      var nickName = $('#islogin_1').text();

      $.get('/collectGoods/?product='+product+'&nickName='+nickName)
   })

    //收藏的商品爱心点亮
    $('.Collect').each(function () {
        var product = $(this).next().next().text();
        var nickName = $('#islogin_1').text();
        var love = $(this);
        var state = love.css('background-position');

        $.ajax({
            url:'/light_collect/?product='+product+'&nickName='+nickName,
            type:'get',
            dataType:'json',
            success:function (msg) {
             if(msg.data == 'Success'){
                  love.css('background-position','right -17px');
              }
            }
        })
    })

});