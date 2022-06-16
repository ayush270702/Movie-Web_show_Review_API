from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'
    
class ReviewDetailThrottle(UserRateThrottle):    
    scope = 'review-detail'