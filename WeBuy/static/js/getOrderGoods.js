$(function () {
   var orderCode =$('#orderCode').text();

   $.get('/getOrderGoods'+orderCode+'/',function (list) {
       $.each(list.data,function (index, item) {
          $('tbody').append('<tr>\n' +
              '                    <td class="Product_info">\n' +
              '                     <a href="#"><img src="/static/media/'+item[0]+'"  width="100px" height="100px"/></a>\n' +
              '                     <a href="#" class="product_name">'+item[1]+'</a>\n' +
              '                     </td>\n' +
              '                    <td><i>￥</i>'+item[2]+'</td>\n' +
              '                    <td><i>￥</i>'+item[2]+'</td>\n' +
              '                    <td>'+item[3]+'</td>\n' +
              '                    <td class="Moneys"><i>￥</i>'+item[4]+'</td>\n' +
              '                   </tr>')

       });
   });

});