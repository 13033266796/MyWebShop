$(function () {
   var  nickName = $('#islogin_1').text();
   $.get('/getMyOrder/',function (list) {

       var info = '';
       $.each(list.data,function (index,item) {
           info += '<tr>\n' +
           '               <td>\n' +
           '                <div class="product_name clearfix">\n' +
           '                    <a href="#"><img src="/static/media/'+item[0]+'"  width="80px" height="80px"/></a>\n' +
           '                    <a href="3">'+item[1]+'</a>\n' +
           '                    <p class="specification">礼盒装20个/盒</p>\n' +
           '                </div>\n' +
           '               </td>\n' +
           '               <td>'+item[2]+'</td>\n' +
           '               <td>'+item[3]+'</td>\n' +
           '                </tr>';
       });


       $('#parent_table').append('<tbody>\n' +
           '           <tr><td colspan="6" class="Order_form_time"><a href="/order'+list.orderCode+'/" style="color: black">'+list.orderCode+'</a></td></tr>\n' +
           '           <tr>\n' +
           '           <td colspan="3">\n' +
           '           <table class="Order_product_style">\n' +
           '           '+info+
           '            </table>\n' +
           '           </td>\n' +
           '           <td class="split_line">'+list.total_pay+'</td>\n' +
           '           <td class="split_line">已发货，待收货</td>\n' +
           '           <td></td>\n' +
           '           </tr>\n' +
           '         </tbody>');


   });

});