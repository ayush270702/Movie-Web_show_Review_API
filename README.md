# Movie-Web_show_Review_API
A REST API providing information about Popular Movies/Web Series, the platform where they are broadcast and their reviews.

# watchmovie
This is the main folder containing settings.py (global settings for whole project), urls.py (connection urls of all the applications present)

# manage.py
This manage.py utility provides various commands that you must have while working with Django

# watchlist_app
This is main app of project which contains StreamPlatform, Review, Watchlist models 
StreamPlatform - contains various streaming channels, information about them and their websites.Only the admin has permission to create, remove or update these.
WatchList - contains different web series and movies, connected to StreamPlatform with foregin key. Only admin has permission to create, delete or update them
Review - contains reviews about different movies and web series connected to User and WatchList with foregin key. Any user can view reviews, only authenticated users can          create a review and the user who creates review and admin can delete and update review

# user_app
It handels Registration, Login and Logout

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------


This project covers many major topics like Authentication, Token authentication, JWT authentication, different permissions, Throttling, Filtering, Searching, Ordering, Pagination, etc. Test cases for automated api testing is also written.
