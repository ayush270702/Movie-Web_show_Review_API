from operator import ge
from watchlist_app.models import *
from watchlist_app.api.serializers import *
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
# from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from watchlist_app.api.throttling import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from watchlist_app.api.pagination import *




class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username=username)

    def get_queryset(self):
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username=username)



class WatchListGV(generics.ListCreateAPIView):
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['avg_rating']
    permission_classes = [AdminOrReadOnly]
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    pagination_class = WatchListCPagination
    
    
class WatchDetailGV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminOrReadOnly]
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    



class StreamPlatformGV(generics.ListCreateAPIView):
    permission_classes = [AdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
class StreamDetailGV(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    


class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(review_user=review_user, watchlist=watchlist)
        
        if review_queryset.exists():
            raise ValidationError("Already Reviewed")
       
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating+serializer.validated_data["rating"])/2
        
        watchlist.number_rating  = watchlist.number_rating + 1
        watchlist.save()        
        
        serializer.save(watchlist=watchlist, review_user=review_user)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ ReviewCreateThrottle,AnonRateThrottle]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['review_user__username', 'active']
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['review_user__username', 'active']

    

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

            
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    # throttle_classes = [ReviewDetailThrottle , AnonRateThrottle]
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    
    permission_classes = [ReviewUserOrReadOnly]
