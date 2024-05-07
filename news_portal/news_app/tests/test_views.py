import pytest
from rest_framework.test import APIClient
from news_app.models import News, Comment


@pytest.mark.django_db
def test_news_list():
    """
    Test the API endpoint for listing all news items.

    This test verifies that the news list endpoint correctly returns a list of all news
    entries in the database and that the response status code is 200 (OK). It also checks
    that the number of news items returned is correct and that the titles of the news items
    match the expected values.

    Assertions:
        - The response status code is 200.
        - The length of the response data matches the number of news items created.
        - The title of each news item in the response matches the title of the created news items.
    """
    # Create an API client instance for making requests.
    client = APIClient()

    # Create two news items in the database.
    News.objects.create(title="News 1", body="Body 1")
    News.objects.create(title="News 2", body="Body 2")

    # Make a GET request to the news list endpoint.
    response = client.get('/api/news/')

    # Check the response status code is 200 (OK).
    assert response.status_code == 200, "Expected response status 200, got {0}".format(
        response.status_code)

    # Check the number of items in the response is 2.
    assert len(response.data) == 2, "Expected 2 news items, got {0}".format(
        len(response.data))

    # Check that the titles of the news items match what was created.
    assert response.data[0]['title'] == "News 1", "Expected title 'News 1', got '{0}'".format(
        response.data[0]['title'])
    assert response.data[1]['title'] == "News 2", "Expected title 'News 2', got '{0}'".format(
        response.data[1]['title'])


@pytest.mark.django_db
def test_comments_list():
    """
    Test the API endpoint for listing all comments.

    This test ensures that the comments list endpoint correctly returns a list of all comments
    for a specific news item and that the response status code is 200. It also verifies the
    accuracy of the content of the comments and their count in the response.

    Assertions:
        - The response status code is 200.
        - The length of the response data matches the number of comments created.
        - The body of each comment in the response matches the expected values.
    """
    # Create an API client instance.
    client = APIClient()

    # Create a news item and two comments associated with it.
    news = News.objects.create(title="News for Comment", body="Body of news")
    Comment.objects.create(news=news, body="First comment")
    Comment.objects.create(news=news, body="Second comment")

    # Make a GET request to the comments list endpoint.
    response = client.get('/api/comments/')

    # Check the response status code is 200 (OK).
    assert response.status_code == 200, "Expected response status 200, got {0}".format(
        response.status_code)

    # Check the number of comments in the response.
    assert len(response.data) == 2, "Expected 2 comments, got {0}".format(
        len(response.data))

    # Check the body of each comment matches what was created.
    assert response.data[0]['body'] == "First comment", "Expected body 'First comment', got '{0}'".format(
        response.data[0]['body'])
    assert response.data[1]['body'] == "Second comment", "Expected body 'Second comment', got '{0}'".format(
        response.data[1]['body'])
