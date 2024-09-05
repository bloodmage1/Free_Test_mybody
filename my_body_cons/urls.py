from django.contrib import admin
from django.urls import path, include

# from main.views import index, bodytype, bodytype_details, bodyimportant, inquires

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('체질유형/', include("bodytype.urls")),
    # path('체질유형/<int:pk>/', bodytype_details),
    # path('체질중요성/', include("bodyimportant.urls")),
    path('문의/', include("inquires.urls")),
]
