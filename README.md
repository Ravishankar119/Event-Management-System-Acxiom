# Event Management System (Acxiom Consulting)

A simple, clean, and user-friendly Event Management System built using **Django**.  
This project includes user authentication, event pages, and a structured UI.

## 🚀 Features

- User Login / Logout system  
- Clean UI with reusable templates  
- Header navigation with authentication check  
- Modular app structure  
- Static files setup (CSS/Images)  
- Django template inheritance (`base.html`)

## 📁 Project Structure
'''
project/
│── core/
│   ├── templates/
│   │   ├── core/
│   │   │   ├── base.html
│   │   │   ├── login.html
│   │   │   ├── welcome.html
│   ├── static/
│   │   ├── core/
│   │   │   └── css/
│   │   │       └── style.css
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│
│── project_name/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
'''


1 git clone <your-repo-url>
cd project-folder
2 Create virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate      # For Windows
3 Install dependencies
bash
Copy code
pip install -r requirements.txt
4 Run migrations
bash
Copy code
python manage.py migrate
5 Start the server
bash
Copy code
python manage.py runserver . 

## Screenshots

<img width="1917" height="656" alt="Screenshot 2025-11-19 010600" src="https://github.com/user-attachments/assets/629bb5e6-c2f3-4456-a78d-b6a753979b36" />
<img width="1919" height="807" alt="Screenshot 2025-11-19 010622" src="https://github.com/user-attachments/assets/82c699f7-1567-446c-bd63-c032e3da35cc" />
<img width="1919" height="1021" alt="Screenshot 2025-11-19 010526" src="https://github.com/user-attachments/assets/6d0a83ba-3ae3-4cf8-afc8-32c6c6d26332" />
