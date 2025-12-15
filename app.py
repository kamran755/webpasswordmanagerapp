from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import sqlite3
import csv
import os

app = Flask(__name__)
app.secret_key = "kamran_secret_key"  # flash messages ke liye


DB_NAME = "passwords_web.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT,
            username TEXT,
            password TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    c = conn.cursor()

    if request.method == "POST":
        website = request.form.get("website", "").strip()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        notes = request.form.get("notes", "").strip()

        if not website or not username or not password:
            flash("Please fill Website, Username, and Password", "warning")
        else:
            c.execute(
                "INSERT INTO passwords (website, username, password, notes) VALUES (?, ?, ?, ?)",
                (website, username, password, notes),
            )
            conn.commit()
            flash(f"Saved: {website}", "success")

        # GET pe redirect for refresh
        conn.close()
        return redirect(url_for("index"))

    # GET: list + search
    query = request.args.get("q", "").strip()
    if query:
        c.execute(
            "SELECT * FROM passwords WHERE website LIKE ? ORDER BY id DESC",
            (f"%{query}%",),
        )
    else:
        c.execute("SELECT * FROM passwords ORDER BY id DESC")

    rows = c.fetchall()
    conn.close()
    return render_template("index.html", passwords=rows, query=query)


@app.route("/delete/<int:pw_id>", methods=["POST"])
def delete_password(pw_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE id = ?", (pw_id,))
    conn.commit()
    conn.close()
    flash("Deleted selected record", "info")
    return redirect(url_for("index"))


@app.route("/export")
def export_csv():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, website, username, password, notes FROM passwords")
    rows = c.fetchall()
    conn.close()

    if not rows:
        flash("No data to export", "warning")
        return redirect(url_for("index"))

    filename = "passwords_export_web.csv"
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Website", "Username", "Password", "Notes"])
        for row in rows:
            writer.writerow([row["id"], row["website"], row["username"], row["password"], row["notes"]])

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
