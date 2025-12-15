`app.py` – main Flask application (routes + database logic)
- `templates/base.html` – Bootstrap layout and styling
- `templates/index.html` – form + table UI

---

##  How to Run Locally

1. **Clone the repo**

git clone https://github.com/your-username/password-manager-web-flask.git
cd password-manager-web-flask

text

2. **Create virtual environment (optional but recommended)**

python -m venv venv
venv/Scripts/activate # Windows

source venv/bin/activate # Linux / macOS
text

3. **Install dependencies**

pip install flask

text

4. **Run the app**

python app.py

text

5. **Open in browser**

http://127.0.0.1:5000/

text

---

##  Usage

1. Fill **Website, Username, Password** (Notes optional) in the form.
2. Click **Save** to store the entry in SQLite.
3. Use the top **Search** box to filter by website.
4. Use **Delete** button to remove specific records.
5. Click **Export CSV** to download all records as `passwords_export_web.csv`.

> Note: This is a demo educational project and does not encrypt stored passwords.  
> Do **not** use real sensitive passwords in a production environment.

---

## 📸 Screenshots (suggested)

- Form + table view (desktop)
- Search in action
- CSV opened in Excel

---

##  Possible Improvements

- User authentication (login system) for protected access  
- Password hashing / encryption
- Pagination and sorting for large datasets
- Docker setup for easy deployment

---



