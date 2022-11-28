import pytest
from space_station.models import Station, Instructions


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name',
    [
        'test_station',
    ]
)
def test_create_station(client, name):
    payload = {'name': name}

    response = client.post('/api/stations/', payload)

    data = response.data

    station = Station.objects.all().first()

    assert response.status_code == 201
    assert data['id'] == station.pk
    assert data['name'] == station.name
    assert data['state'] == station.state


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name',
    [
        'test_station',
    ]
)
def test_get_station_detail(client, station, name):
    station = station(name=name)

    response = client.get(f'/api/stations/{station.pk}/')

    data = response.data

    assert response.status_code == 200
    assert data['id'] == station.pk
    assert data['name'] == station.name
    assert data['state'] == station.state


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name',
    [
        'test_station',
    ]
)
def test_station_update(client, station, name):
    station = station(name=name)

    payload = {'name': 'update test_station'}

    response = client.patch(f'/api/stations/{station.pk}/', payload)

    station.refresh_from_db()

    assert response.status_code == 200
    assert station.name == payload['name']


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name',
    [
        'test_station',
    ]
)
def test_station_delete(client, station, name):
    station = station(name=name)

    response = client.delete(f'/api/stations/{station.pk}/')

    assert response.status_code == 204

    with pytest.raises(station.DoesNotExist):
        station.refresh_from_db()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'name, username, password, axis, distance',
    [
        ('test_station', 'test_user', 'test_password', 'x', '-1000'),
        ('test_station', 'test_user', 'test_password', 'y', '-1000'),
        ('test_station', 'test_user', 'test_password', 'z', '-1000'),
    ]
)
def test_station_state(client, user, station, name, username, password, axis, distance):
    user = user(username, password)
    station = station(name)
    payload = {
        "user": user.pk,
        "station": station.pk,
        "axis": axis,
        "distance": distance
    }

    client.post(f'/api/stations/{station.pk}/state/', payload)

    station.refresh_from_db()

    assert station.state == 'broken'
