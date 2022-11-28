from rest_framework.test import APIClient
import pytest
from space_station.models import Station, Instructions
from django.contrib.auth.models import User


@pytest.fixture()
def client() -> APIClient:
    return APIClient()


@pytest.fixture()
def station():
    def create_station(name: str) -> Station:
        station = Station.objects.create(name=name)
        return station

    return create_station


@pytest.fixture()
def instruction():
    def create_instruction(user: int, station: int, axis: str, distance: int) -> Instructions:
        instruction = Instructions.objects.create(user=user, station=station, axis=axis, distance=distance)
        return instruction

    return create_instruction


@pytest.fixture()
def user():
    def create_user(username: str, password: str) -> User:
        user = User(username=username)
        user.set_password(password)
        user.save()

        return user
    return create_user
