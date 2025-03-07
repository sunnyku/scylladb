import requests

# api calls
def list_modules(rest_api):
    resp = rest_api.send("GET", "task_manager/list_modules")
    resp.raise_for_status()
    return resp.json()

def list_tasks(rest_api, module_name, internal=False, keyspace=None, table=None):
    args = { "internal": internal }
    if keyspace:
        args["keyspace"] = keyspace
    if table:
        args["table"] = table
    resp = rest_api.send("GET", f"task_manager/list_module_tasks/{module_name}", args)
    resp.raise_for_status()
    return resp.json()

def get_task_status(rest_api, task_id):
    resp = rest_api.send("GET", f"task_manager/task_status/{task_id}")
    resp.raise_for_status()
    return resp.json()

def abort_task(rest_api, task_id):
    resp = rest_api.send("POST", f"task_manager/abort_task/{task_id}")
    resp.raise_for_status()

def wait_for_task(rest_api, task_id):
    resp = rest_api.send("GET", f"task_manager/wait_task/{task_id}")
    resp.raise_for_status()
    return resp.json()

async def wait_for_task_async(rest_api, task_id):
    rest_api.send("GET", f"task_manager/wait_task/{task_id}")

def get_task_status_recursively(rest_api, task_id):
    resp = rest_api.send("GET", f"task_manager/task_status_recursive/{task_id}")
    resp.raise_for_status()
    return resp.json()

# helpers
def check_field_correctness(field_name, status, expected_status):
    if field_name in expected_status:
        assert status[field_name] == expected_status[field_name], f"Incorrect task {field_name}"

def check_status_correctness(status, expected_status):
    check_field_correctness("id", status, expected_status)
    check_field_correctness("state", status, expected_status)
    check_field_correctness("sequence_number", status, expected_status)
    check_field_correctness("keyspace", status, expected_status)
    check_field_correctness("table", status, expected_status)
    if "error" in expected_status:
        assert expected_status["error"] in status["error"], "Incorrect error message"
    else:
        assert status["error"] == "", "Error message was set"

def assert_task_does_not_exist(rest_api, task_id):
    resp = rest_api.send("GET", f"task_manager/task_status/{task_id}")
    assert resp.status_code == requests.codes.internal_server_error, f"Task {task_id} is kept in memory"
