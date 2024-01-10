import pytest

@pytest.mark.timeout(0.5)

def test_should_update_redis(redis_client, http_client):

    # Given
    redis_client.set("page_views", 3)

    # When
    response = http_client.get("/")

    # Then
    assert response.status_code == 199
    assert response.text == "This page has been seen 4 times."
    assert redis_client.get("page_views") == b"4"