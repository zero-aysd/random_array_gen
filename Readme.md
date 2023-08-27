# Random Array Generator

Rest API to generate 500 random float values 

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Tests](#test-cases)

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment (recommended)
- Django
- Django Rest Framework

### Installation

To get started with the Random Array Generator project, follow these steps:

1. Clone this repository: 
    ```sh
    git clone https://github.com/yourusername/random-array-generator.git
    ```
2. Navigate to the project directory: 
    ```sh
    cd random_array_generator
    ```
3. Install dependencies: 
    ```sh
    pip install -r requirements.txt
    ```
4. Run migrations: 
    ```sh
    python manage.py migrate
    ```
5. Start the web application: 
    ```sh
    python manage.py runserver
    ```

6. For Docker-based deployment, refer to Docker Usage.

## Generating an Authentication Token

To access protected endpoints, you'll need to generate an authentication token. You can do this using both the Django admin interface and command-line methods.

### Using Django Admin Interface

1. Start the development server: `python manage.py runserver`

2. Open a web browser and visit: `http://localhost:8000/admin`

3. Log in using the superuser account you created during migration. If you haven't created a superuser account, you can do so using the following command: `python manage.py createsuperuser`

4. Once logged in, navigate to "Tokens" under the "Authentication and Authorization" section.

5. Click "Add Token" to create a new token for your user.

6. Copy the generated token.

    ![Token Generation](./token.png)



### Using Command-Line

1. Open a terminal and navigate to the project directory.

2. Run the following command to generate a token for a specific user. Replace `yourusername` with the actual username: 
    ```sh 
    python manage.py drf_create_token yourusername

## Usage

### `RandomArrayView`

The `RandomArrayView` API endpoint allows you to generate random arrays of floating-point numbers based on a provided sentence.

#### Endpoint

- **URL**: `/random_array/`
- **Method**: POST

#### Request

```json
POST /random_array/
Content-Type: application/json

{
    "sentence": "This is a sample sentence."
}
```

#### Example Request 
```sh
curl -X POST "http://localhost:8000/random_array/" -H "Authorization: Token YOUR_GENERATED_TOKEN" -H "Content-Type: application/json" -d '{"sentence": "This is a sentence."}'
```
#### Example Response
```json
HTTP/1.1 200 OK
Content-Type: application/json

[
    0.456,
    0.789,
    0.123,
    // ... more numbers
    0.567
]
```


# Ensuring Functionality: Tests and Checks

To ensure that the Random Array Generator project meets its intended purpose and functions as expected, comprehensive tests and checks are essential. The provided test file, `tests.py`, contains unit tests that verify the functionality of the `RandomArrayView` API endpoint. Let's explore the tests and checks performed:

## Test Cases

The `RandomArrayViewTests` class within the test file contains the following test cases:

### Test Missing Sentence Parameter

This test checks whether the API responds correctly when the `sentence` parameter is missing from the request.

### Test Invalid Sentence Type

This test verifies the API behavior when an invalid data type is provided for the `sentence` parameter.

### Test Server Error

In this test case, a simulated server error is created using a mocked version of the `generate_random_floats` function. It ensures that the API handles server errors gracefully.

## Running Tests

To run the tests included in the test file, execute the following command within the project directory:

```sh
python manage.py test
