from django.urls import path
from mathapp import views

urlpatterns=[
    path('cal/add',views.AddView.as_view(),name="addition"),
    path('cal/sub',views.SubView.as_view(),name="subtraction"),
    path('cal/mul',views.mul,name="multiplication"),
    path('cal/div',views.divi,name="division"),
    path('cal/cube',views.cube,name="cube"),
    path('cal/square',views.square,name="square"),
    path('',views.home,name='home'),
    path('ebill',views.ebill,name="ebill"),
    path('donation',views.donation,name='donation'),
    path('parking',views.parking,name='parking')
]