from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.index, name='index'),
    path('getDetails',views.getDetails, name='getDetails'),
    path('home',views.index, name='home'),
    path('upload',views.uploadImage,name='uploadImage'),
    # path(r'/(?P<slug>.*)/',views.predict_disease,name='image_classifer'),
    #  path('image_classifer/<slug:image>/',views.predict_disease)
    # path('image_classifer/(?P<slug>[\w-]+)/$',views.predict_disease,name='image_classifer')
  
    # path('predict',views.predict_disease,name='predict'),
    path('aboutus',views.aboutus,name='aboutus'),
    # path('getDetails',views.test_url,name='getDetails'),
    path('help',views.help,name='help')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)