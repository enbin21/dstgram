from django.urls import path
from .views import *
from .models import Photo

app_name = 'photo'

urlpatterns = [
    # path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', login_required(DetailView.as_view(model=Photo, template_name='photo/detail.html')), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('', PhotoListView.as_view(), name='photo_list'),
    path('profile/', profile_view, name='profile'),
    path('myphoto/', PhotoMyList.as_view(), name='myphoto'),
]