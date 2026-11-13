

import pytest, requests

#1
def test_get_all_bookings_200(base_url):
    r = requests.get(f"{base_url}/booking/")
    assert (r.status_code == 200) and (len(r.json()) != 0)

#2
def test_post_booking_200(base_url,booking_data, token):
    r = requests.post(f"{base_url}/booking/",json=booking_data)
    status = r.status_code
    data = r.json()
    id = data["bookingid"]
    requests.delete(f"{base_url}/booking/{id}", cookies={"token":token})
    assert (status == 200) and (data["booking"] == booking_data )
    

#3
def test_get_created_booking(base_url,create_booking, booking_data):
    booking_id = create_booking
    r = requests.get(f"{base_url}/booking/{booking_id}")
    data = r.json()
    assert ( (r.status_code == 200) and 
            (data["firstname"] == booking_data["firstname"]) and
            (data["lastname"] == booking_data["lastname"]) and 
            (data["totalprice"] == booking_data["totalprice"]) )

#4
def test_put_firstname_booking_with_token(base_url,booking_data,create_booking,token):
    booking_id = create_booking
    new_name = "NewTester"
    new_booking = booking_data
    new_booking["firstname"] = new_name
    r = requests.put(f"{base_url}/booking/{booking_id}", json=new_booking, cookies={"token":token})
    assert ( (r.json()["firstname"] == new_name) and (r.status_code == 200) )

    
#5
def test_patch_lastname_booking_with_token(base_url,create_booking,token,booking_data):
    booking_id = create_booking
    new_lastname = "NewUser"
    r = requests.patch(f"{base_url}/booking/{booking_id}", json={"lastname":new_lastname}, cookies={"token":token})
    data = r.json()
    assert ( (r.status_code == 200) and 
            ( data["firstname"] == booking_data["firstname"] ) and 
            ( data["lastname"] == new_lastname ) )

   
#6 (PART 1: status code of get after deleting is valid?)BUG HERE
def test_get_after_delete_booking_with_token(base_url,create_booking,token):
    booking_id = create_booking
    r = requests.delete(f"{base_url}/booking/{booking_id}", cookies={"token":token})
    r = requests.get(f"{base_url}/booking/{booking_id}")
    get_after_delete_status = r.status_code
    assert (get_after_delete_status == 404)

#6 (PART 2: status code of delete is valid?)BUG HERE
@pytest.mark.xfail(reason="Status code returns 201 instead of 200 or 204 when deleting with valid token")
def test_delete_booking_with_token(base_url,create_booking,token):
    booking_id = create_booking
    r = requests.delete(f"{base_url}/booking/{booking_id}", cookies={"token":token})
    delete_status = r.status_code
    assert ( (delete_status == 200) or (delete_status == 204) )

#7
def test_put_firstname_booking_without_token(base_url,create_booking):
    booking_id = create_booking
    new_name = "NewTester"
    r = requests.put(f"{base_url}/booking/{booking_id}", json={"firstname":new_name})
    assert r.status_code == 403


#8
def test_get_booking_99999(base_url):
    r = requests.get(f"{base_url}/booking/999999999")
    assert r.status_code == 404


#9 (Part 1: Status Code) BUG HERE
@pytest.mark.xfail(reason="Status code returns 200 instead of 400 or 401 while having wrong password input")
def test_post_status_code_auth_wrong_password(base_url):
    r = requests.post(f"{base_url}/auth", json={"username":"admin",
                                                "password":"12345678"})
    assert ((r.status_code == 400) or (r.status_code == 401))


#9 (Part 2: Response Body Matches)
def test_post_response_auth_wrong_password(base_url):
    r = requests.post(f"{base_url}/auth", json={"username":"admin",
                                                "password":"12345678"})
    assert (r.json()["reason"] == "Bad credentials")


#10
def test_get_booking_using_query_param_firstname(base_url,create_booking):
    booking_id = create_booking
    filter_by_name = "Test"
    r = requests.get(f"{base_url}/booking?firstname={filter_by_name}")
    assert (r.status_code == 200) and (any(r.json()[x]["bookingid"] == booking_id for x in range(len(r.json()))))
