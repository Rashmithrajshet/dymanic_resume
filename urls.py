from django.contrib import admin
from django.urls import path
from resume.views import signup,login,form,resume,home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path("",home,name='home'),
    path('form/<int:user_id>/',form, name='form'),
    path('resume/<int:user_id>/',resume, name='resume'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
