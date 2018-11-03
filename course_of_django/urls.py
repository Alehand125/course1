from django.conf.urls import include, url
from django.contrib import admin
from test1 import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'course_of_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^summa/(?P<a>\d+)/(?P<b>\d+)/$', views.summa),
]
