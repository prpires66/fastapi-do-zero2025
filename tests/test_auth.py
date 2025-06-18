from http import HTTPStatus


def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    json_response = response.json()

    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in json_response
    assert json_response['token_type'] == 'bearer'
