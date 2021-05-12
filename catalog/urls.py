
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pieces/', views.PieceListView.as_view(), name='pieces'),
    path('piece/<int:pk>/recording', views.recording_detail_view, name='recording'),
    path('piece/<int:pk>', views.PieceDetailView.as_view(), name='piece-detail'),
    path('composers/', views.ComposerListView.as_view(), name='composers'),
    path('composer/<int:pk>', views.ComposerDetailView.as_view(), name='composer-detail'),
]
