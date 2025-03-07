# Django Project

This is a Django project with User and Product models, including APIs for user management and fetching the top 3 most expensive products.

## Features
- User management API (GET, POST)
- Product management API (GET top 3 expensive products)
- String reversal function

## Installation

### Prerequisites
- Python 3.11+
- Django
- Django REST Framework

### Setup
1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd project
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### User API
- **GET /api/users/** → Fetch all users
- **POST /api/users/** → Create a new user

### Product API
- **GET /api/top-products/** → Get top 3 most expensive products

### String Reversal API
- **GET /reverse/** → Returns reversed words from "Hello World Python"

## Usage
- Access Django Admin Panel: `http://127.0.0.1:8000/admin/`
- Use Postman or Curl to test APIs


