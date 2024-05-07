from django.db import models

# models.py: Defines the data models for the "news" app in a Django project.


class News(models.Model):
    """
    Represents a news article in the database.

    Attributes:
        title (models.CharField): The title of the news article.
        body (models.TextField): The full text content of the news article.
        created_at (models.DateTimeField): The date and time the article was created, automatically set to the current time when the article is first created.

    Methods:
        __str__(self): Returns a human-readable string representation of the model, which is the title of the news article.
    """
    # Title of the news article, up to 511 characters.
    title = models.CharField(max_length=511)

    # Main content or body of the news article.
    body = models.TextField()

    # Timestamp indicating when the article was created. Automatically set to the time the record is created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return the title, which is a meaningful representation of the object
        return self.title


class Comment(models.Model):
    """
    Represents a comment made on a news article in the database.

    Attributes:
        news (models.ForeignKey): A foreign key to the News model, establishing a many-to-one relationship where each news article can have many comments.
        body (models.TextField): The text content of the comment.
        created_at (models.DateTimeField): The date and time the comment was created, automatically set to the current time when the comment is first created.

    Methods:
        __str__(self): Returns a human-readable string representation of the model, which is a descriptor of the comment relative to the news article it belongs to.
    """
    # ForeignKey link to the News model, establishing a many-to-one relationship.
    # 'related_name' allows access to comments from the News instance (news.comments).
    # 'on_delete=models.CASCADE' ensures that comments are deleted if the related news article is deleted.
    news = models.ForeignKey(
        News, related_name='comments', on_delete=models.CASCADE)

    # Content of the comment.
    body = models.TextField()

    # Timestamp indicating when the comment was created. Automatically set to the time the record is created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Returns a string that describes the comment in context of the news article it belongs to.
        return f"Comment on {self.news.title}"
