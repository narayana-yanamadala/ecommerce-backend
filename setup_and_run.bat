@echo off
echo =============================================
echo   Multimart - Django Backend Setup
echo =============================================
cd /d "%~dp0"

echo [1/6] Creating virtual environment...
python -m venv venv

echo [2/6] Activating...
call venv\Scripts\activate

echo [3/6] Installing packages...
pip install django djangorestframework django-cors-headers requests setuptools

echo [4/6] Running migrations...
python manage.py makemigrations
python manage.py makemigrations orders
python manage.py migrate
python manage.py createcachetable

echo [5/6] Creating superuser...
python manage.py createsuperuser

echo [6/6] Seeding 50+ products...
python seed_products.py

echo.
echo =============================================
echo  Server: http://127.0.0.1:8000
echo  Admin:  http://127.0.0.1:8000/admin
echo =============================================
python manage.py runserver
pause
