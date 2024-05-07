from rest_framework import viewsets
from .models import News, Comment
from .serializers import NewsSerializer, CommentSerializer

# views.py: Defines the viewsets for the "news" app in a Django REST Framework project.


class NewsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing news instances.

    Attributes:
        queryset (queryset): A queryset that represents all news instances. 
                             This queryset is evaluated lazily, meaning it doesn't hit the database 
                             until it's evaluated. This allows filtering and other modifications 
                             without cost until execution.
        serializer_class (NewsSerializer): Specifies the serializer to use for handling 
                                           serialization and deserialization of News instances.
                                           This connects the model instance with the corresponding 
                                           serializer for data validation and query handling.

    Methods:
        Inherits all methods from `ModelViewSet` which include `create()`, `retrieve()`, 
        `update()`, `partial_update()`, `destroy()` and `list()` operations by default.
    """
    queryset = News.objects.all()  # Retrieve all news instances from the database.
    # Connect the News model with the NewsSerializer.
    serializer_class = NewsSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment instances.

    Attributes:
        queryset (queryset): A queryset that represents all comment instances. 
                             This queryset is used by the viewset to perform query operations 
                             like filtering and ordering. It’s optimized for read operations 
                             and provides various data manipulation capabilities.
        serializer_class (CommentSerializer): Defines the serializer to use for handling 
                                              serialization and deserialization of Comment 
                                              instances. The serializer allows for data 
                                              validation and formatting based on the model.

    Methods:
        Inherits from `ModelViewSet` which automatically provides `create`, `retrieve`, 
        `update`, `partial_update`, `destroy` and `list` actions.
    """
    queryset = Comment.objects.all()  # Retrieve all comment instances from the database.
    # Associate Comment model instances with CommentSerializer.
    serializer_class = CommentSerializer
