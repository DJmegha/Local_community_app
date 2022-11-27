from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('AboutUs',views.AboutUs,name='AboutUs'),
    path('ServiceList',views.Service_list,name='ServiceList'),
    path('ServiceCategory/<int:id>/',views.Service_Category,name='ServiceCategory'),
    path('ServiceProvider/<int:id>/',views.Service_provider,name='ServiceProvider'),
    path('ServiceDetail/<int:pk>/',views.ServiceDetail,name='ServiceDetail'),
    path('Service/new/',views.NewServiceProvider,name='Service_new'),
    path('ContactUs',views.ContactUs,name='ContactUs'),
    path('register/',views.register_user,name='register'),
    path('postComment/<int:pk>/', views.postComment, name="postComment"),
     path('AddService/new/',views.AddNewService,name='AddService_new'),
    #  path('comment',views.comment,name='comment'),
]
