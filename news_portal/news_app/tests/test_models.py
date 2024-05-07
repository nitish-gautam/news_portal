from news_app.models import News, Comment
import pytest
import django

# Setup Django environment to ensure models and other settings are properly initialized.
django.setup()


@pytest.mark.django_db
def test_create_news():
    """
    Test case for creating a News instance and asserting its properties.

    This test ensures that a News instance can be successfully created with specified
    title and body, and that it is correctly stored in the database with the auto-set
    created_at field populated.

    Assertions:
        - The title of the News instance matches the provided input.
        - The body of the News instance matches the provided input.
        - The created_at field of the News instance is automatically populated, confirming
          that the database is handling it as expected.
    """
    # Create a News instance with a specific title and body.
    news = News.objects.create(
        title="Sample News", body="This is a sample news body.")

    # Assertions to verify that the news instance is created as expected.
    assert news.title == "Sample News", "The news title does not match the expected value."
    assert news.body == "This is a sample news body.", "The news body does not match the expected value."
    assert news.created_at is not None, "The news created_at field should be automatically populated."


@pytest.mark.django_db
def test_create_comment():
    """
    Test case for creating a Comment instance related to a News instance and asserting its properties.

    This test validates that a Comment instance can be successfully created with a reference
    to a specific News instance and contains the correct body text. It also verifies that
    the created_at field is automatically set upon creation.

    Assertions:
        - The body of the Comment instance matches the provided input.
        - The Comment instance is linked to the correct News instance.
        - The created_at field of the Comment instance is not None, ensuring it is automatically set.
    """
    # Create a News instance to which the comment will be linked.
    news = News.objects.create(title="Sample News", body="News body here.")

    # Create a Comment instance linked to the previously created news instance.
    comment = Comment.objects.create(news=news, body="A sample comment.")

    # Assertions to verify that the comment instance is created as expected.
    assert comment.body == "A sample comment.", "The comment body does not match the expected value."
    assert comment.news == news, "The comment is not linked to the correct news instance."
    assert comment.created_at is not None, "The comment created_at field should be automatically populated."
