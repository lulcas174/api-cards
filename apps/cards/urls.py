from django.urls import path
from .views import CardCreateAPIView, CardUploadAPIView, CardDetailAPIView, CardListAPIView

urlpatterns = [
    path('create/', CardCreateAPIView.as_view(), name='create-card'),
    path('upload/', CardUploadAPIView.as_view(), name='upload-cards'),
    path('detail/<str:number>/', CardDetailAPIView.as_view(), name='detail-card'),
    path('list/', CardListAPIView.as_view(), name='list-cards'),
]
