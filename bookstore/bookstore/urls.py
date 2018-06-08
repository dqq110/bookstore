from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls', namespace='user')), # 用户模块
    url(r'^tinymce/', include('tinymce.urls')), # 富文本编辑器
    url(r'^', include('books.urls', namespace='books')), # 商品模块
    url(r'^cart/', include('cart.urls', namespace='cart')), # 购物车模块
    url(r'^order/', include('order.urls', namespace='order')), # 订单模块
    url(r'^search/',include('haystack.urls')),
    url(r'^comment/',include('comments.urls',namespace='comment'))
]
