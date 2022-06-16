from django.urls import path, include
from watchlist_app.api.views import *

urlpatterns = [
    path('list/', WatchListGV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailGV.as_view(), name='watch-detail'),
    
    path('stream/', StreamPlatformGV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamDetailGV.as_view(), name='stream-detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    
    path('review/', UserReview.as_view(), name='user-review'),
    # path('review/<str:username>/', UserReview.as_view(), name='user-review'),
    
    
]
