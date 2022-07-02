from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='home'),













    #  Templates urls
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('right/',views.right,name='right'),
    path('bloggrid/',views.bloggrid,name='bloggrid'),
    path('bloglist/',views.bloglist,name='bloglist'),
    path('blogfull/',views.blogfull,name='blogfull'),
    path('pagecontact/',views.pagecontact,name='pagecontact'),
    path('pageaccount/',views.pageaccount,name='pageaccount'),
    path('loginregister/',views.loginregister,name='loginregister'),
    path('pagepurchase/',views.pagepurchase,name='pagepurchase'),
    path('page404/',views.page404,name='page404'),
    path('shopwishlist/',views.shopwishlist,name='shopwishlist'),
    path('shopcart/',views.shopcart,name='shopcart'),
    path('compare',views.compare,name='compare'),
    path('newslatter',views.newslatter,name='newslatter'),
]