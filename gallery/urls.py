from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('', views.home,name="home"),
    path('register',views.register, name="register"),
    path('login',views.login, name="login"),
    path('logout_view',views.logout_view, name="logout_view"),
    path('imagegallery',views.imagegallery, name='imagegallery'),
    path('profile',views.profile, name='profile'),
    path('update_profile',views.update_profile, name='update_profile'),
    path('feedbacks',views.feedbacks, name='feedbacks'),
    path('update_password',views.update_password, name='update_password'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)