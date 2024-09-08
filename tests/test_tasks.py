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
