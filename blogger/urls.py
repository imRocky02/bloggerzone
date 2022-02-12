from django.contrib import admin
from django.urls import path, include
# from django.urls.conf import include, include


admin.site.site_header = "Blogger Admin"
admin.site.site_title = "Blogger Admin"
admin.site.index_title = "Blogger Admin"

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('accounts.urls')),

]
