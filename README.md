# 🗓️ Django Monthly Challenges App

A simple Django web application that displays a list of monthly challenges.  
Each month links to its own dedicated page where users can view a motivational or themed challenge for that month.

This project helped me practice Django templates, static files, and the Django Template Language (DTL).

---

## 🚀 Features
- Dynamic routing for monthly challenges  
- Template inheritance using a shared `base.html`  
- Reusable components (navigation, headers, footers)   
- Custom app-level static files for modular styling  
- 404 error page for invalid months  

---

## 🛠️ Tech Stack
- **Backend:** Django 5.2.7 (Python 3.12)  
- **Frontend:** HTML, CSS
- **Database:** SQLite (default Django DB)  
- **Environment Management:** Virtual Environment + `requirements.txt`  
- **Dependencies:** asgiref, sqlparse, tzdata, pillow  

---

## ⚙️ Installation & Setup

1. **Clone the repository**  
   ```
   git clone https://github.com/yourusername/monthly-challenges.git
   cd monthly-challenges
   ```
---

2. **Create and activate a virtual environment**  
   ```
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```
---

3. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```
---

4. **Run database migrations**  
   ```
   python manage.py migrate
   ```
---

5. **Start the development server**  
   ```
   python manage.py runserver
   ```
---

6. **Access the app**  
   - Main form: http://127.0.0.1:8000  
   - Admin panel: http://127.0.0.1:8000/challenges/january
---

## 🧩 Project Structure
```
monthly-challenges/
├── challenges/
│   ├── migrations/
│   ├── templates/
│   │   ├── challenges/
│   │   │   ├── index.html
│   │   │   ├── challenge.html
│   │   │   └── 404.html
│   ├── static/
│   │   ├── challenges/
│   │   │   ├── styles.css
│   │   │   └── images/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   └── models.py
│
├── templates/
│   └── base.html
│
├── static/
│   └── styles.css
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```
---

## 🧠 Learning Outcomes
Through this project, I learned how to:
- Use Django Template Language (DTL) to render dynamic data
- Implement template inheritance and include reusable components
- Serve and organize static files globally and per app
- Build dynamic URLs using {% url %}
- Handle invalid routes with custom 404 pages
- Style pages using custom CSS

---

## 👤 Author

Kyriakos Ververidis
📍 Based in Greece
💬 Open to remote opportunities
📧 ververidiskyriakos@gmail.com
🔗 https://www.linkedin.com/in/kyriakos-ververidis-593a8561/

---

##📝 License

This project is open-source and free to use for educational purposes.
**License:** MIT License – see [LICENSE](LICENSE) for details.



