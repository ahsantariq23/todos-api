import requests

# Define the base URL of your Flask API
BASE_URL = 'http://localhost:8088'

def test_post_todo():
    # Define the endpoint for creating a new todo
    endpoint = '/todo/4'  # Assuming you want to add a new todo with ID 4

    # Sample data for the new todo
    data = {
        "task": "Study for exam",
        "summary": "Prepare for upcoming exams"
    }

    # Send a POST request to create a new todo
    response = requests.post(BASE_URL + endpoint, json=data)

    # Print the response
    print("Response status code:", response.status_code)
    print("Response body:", response.json())

def test_put_todo():
    # Define the endpoint for updating an existing todo
    endpoint = '/todo/2'  # Assuming you want to update the todo with ID 4

    # Updated data for the todo
    data = {
        "task": "ppppppppppppppppp",
        "summary": "ppppppppppppppppppppppp"
    }

    # Send a PUT request to update the todo
    response = requests.put(BASE_URL + endpoint, json=data)

    # Print the response
    print("Response status code:", response.status_code)
    print("Response body:", response.json())

if __name__ == '__main__':
    test_put_todo()
