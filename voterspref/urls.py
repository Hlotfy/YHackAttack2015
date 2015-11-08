from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'voterspref.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'survey.views.home', name='home'),
    url(r'^thanks/', 'survey.views.home', name='home'),
    url(r'^survey/', 'survey.views.some_view'),
    url(r'^admin/', include(admin.site.urls)),
]
