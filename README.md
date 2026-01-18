# Car Rent — Setup & Run

Prerequisites
- Python 3.8+ installed
- MySQL server running (or update `get_db_connection()` in `apps.py`)

Quick install (Windows PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

Quick install (macOS / Linux)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Environment variables (examples)
- Windows PowerShell:
```powershell
$env:SECRET_KEY = 'your-secret'
$env:ADMIN_EMAIL = 'admin@example.com'
$env:ADMIN_PASSWORD = 'password'
$env:CASHFREE_CLIENT_ID = '...'
$env:CASHFREE_SECRET = '...'
```
- macOS / Linux:
```bash
export SECRET_KEY='your-secret'
export ADMIN_EMAIL='admin@example.com'
export ADMIN_PASSWORD='password'
export CASHFREE_CLIENT_ID='...'
export CASHFREE_SECRET='...'
```

Database
- Create a database named `mydatabase` (or change `get_db_connection()` in `apps.py`). Example SQL:
```sql
CREATE DATABASE mydatabase;
USE mydatabase;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  password VARCHAR(255)
);
CREATE TABLE admin (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255),
  password VARCHAR(255)
);
CREATE TABLE bookings (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  pickup_location VARCHAR(255),
  dropoff_location VARCHAR(255),
  pickup_date DATE,
  dropoff_date DATE,
  booking_date VARCHAR(50),
  car_type VARCHAR(50),
  full_name VARCHAR(255),
  email VARCHAR(255),
  phone VARCHAR(50),
  car_quantity INT,
  amount DECIMAL(10,2),
  payment_status VARCHAR(50),
  booking_status VARCHAR(50)
);
```

Run the app
- From an activated virtualenv run:
```bash
python apps.py
```
Then open: http://127.0.0.1:5000

Notes
- The project currently uses `app.run(debug=True)` in `apps.py` (development). For production use a proper WSGI server and set a secure `SECRET_KEY` and real DB credentials.
- To pin exact dependency versions run `pip freeze > requirements.txt` on your machine and commit the file.
