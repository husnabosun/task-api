import requests
import pytest
BASE_URL = "http://localhost:3000"
INVALID_IDS = [9999, -1, 0, 1000000]

# pytest automatically finds files that start with test_ (or end with _test.py)
# and runs functions inside them start with test_
def create_and_get_task_id(title="Test task"):
    response = requests.post(f"{BASE_URL}/tasks", json={"title": title})
    return response.json()["id"]

def test_get_all_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    # all tesk items are stored in a list according to the contract
    assert isinstance(response.json(), list)

@pytest.mark.parametrize("task_id", [1, 2])
def test_get_single_task_found(task_id):
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200, f"Task {task_id} might not exist or endpoint is broken."
    body = response.json()
    assert isinstance(body, dict)
    assert body["id"] == task_id

@pytest.mark.parametrize("bad_id", INVALID_IDS)
def test_get_single_task_not_found(bad_id):
    response = requests.get(f"{BASE_URL}/tasks/{bad_id}")
    assert response.status_code == 404
    assert "error" in response.json()
    
def test_create_task():
    response = requests.post(f"{BASE_URL}/tasks", json={"title" : "New task from test"})
    assert response.status_code == 201
    res_body = response.json()
    assert res_body["title"] == "New task from test"
    assert res_body["done"] == False
    assert "id" in res_body

@pytest.mark.parametrize("update_payload", [
    {"done" : True}, 
    {"title": "Updated title"},
    {"title" : "Updated both", "done": True}
])
def test_update_task_found(update_payload):
    created_id = create_and_get_task_id()  
    response = requests.put(f"{BASE_URL}/tasks/{created_id}", json=update_payload)
    assert response.status_code == 200
    res_body = response.json()
    for key, value in update_payload.items():
        assert res_body[key] == value

@pytest.mark.parametrize("bad_id", INVALID_IDS)
def test_update_task_not_found(bad_id):
    response = requests.put(f"{BASE_URL}/tasks/{bad_id}", json={"done" : True})
    assert response.status_code == 404

def test_delete_task():
    task_id = create_and_get_task_id()
    
    delete_response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert delete_response.status_code == 204
    
    get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert get_response.status_code == 404

@pytest.mark.parametrize("bad_id", INVALID_IDS)
def test_delete_task_not_found(bad_id):
    response = requests.delete(f"{BASE_URL}/tasks/{bad_id}")
    assert response.status_code == 404