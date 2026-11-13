

import pytest, requests

@pytest.fixture
def base_url():
    return "https://restful-booker.herokuapp.com"


@pytest.fixture
def booking_data():
    return ({"firstname" : "Test",
        "lastname" : "User",
        "totalprice" : 911,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Lunch"
        }
    )


@pytest.fixture
def token(base_url):
    r = requests.post(f"{base_url}/auth", json={"username":"admin", "password":"password123"})
    return r.json()["token"] #returns the response value having key="token"


@pytest.fixture
def create_booking(base_url,booking_data,token):

    r = requests.post(f"{base_url}/booking", json=booking_data)
    booking_id = r.json()["bookingid"]
    yield booking_id
    requests.delete(f"{base_url}/booking/{booking_id}",cookies={"token":token})

