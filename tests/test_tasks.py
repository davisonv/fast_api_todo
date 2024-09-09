def test_create_task(client):
    response = client.post(
        '/tasks/',
        json={
            'title': 'Test todo',
            'description': 'Test todo description',
            'completed': False,
        },
    )
    assert response.json() == {
        'id': 1,
        'title': 'Test todo',
        'description': 'Test todo description',
        'completed': False,
    }


def test_put_task(client):
    response = client.put(
        '/tasks/1',
        json={
            'title': 'Test todo put',
            'description': 'Test todo put description',
            'completed': False,
        },
    )
    assert response.json() == {
        'id': 1,
        'title': 'Test todo put',
        'description': 'Test todo put description',
        'completed': False,
    }
