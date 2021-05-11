
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('pieces/',views.PieceListView.as_view(), name='pieces'),
    path('composers/',views.ComposerListView.as_view(), name='composers'),
    path('piece/<int:pk>', views.PieceDetailView.as_view(), name='piece-detail'),
    path('composer/<int:pk>', views.ComposerDetailView.as_view(), name='composer-detail'),
]
