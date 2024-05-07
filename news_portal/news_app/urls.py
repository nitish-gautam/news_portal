from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, CommentViewSet

# urls.py: Defines URL routes for the "news" application. Utilizes Django REST Framework's routing system to handle API endpoints.

# Create a router instance from DefaultRouter which automatically creates routes for standard CRUD operations provided by Django REST Framework's viewsets.
router = DefaultRouter()

# Register the NewsViewSet with the router. This registration tells the router to manage all typical CRUD endpoints for news items,
# such as creating a news item, retrieving news items, updating, and deleting them.
# 'r'news'' specifies the base portion of the URL path for these operations.
router.register(r'news', NewsViewSet)

# Register the CommentViewSet with the router. Similar to NewsViewSet, this handles all CRUD operations for comments on news items.
# 'r'comments'' sets the base URL path for comment operations.
router.register(r'comments', CommentViewSet)

# urlpatterns: A list of URL patterns for the Django application.
# The 'api/' path includes all routes defined by the router under a common base path, which is prefixed by 'api/' in this case.
# This means all endpoints managed by the router will start with '/api/' followed by further specific paths (e.g., '/api/news/', '/api/comments/').
urlpatterns = [
    # Include the router-generated URL conf. This includes the registered viewsets' routes.
    path('api/', include(router.urls)),
]
