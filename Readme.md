# Random Array Generator

Rest API to generate 500 random float values 

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)


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