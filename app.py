import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)

app.secret_key = "cs50-final-project"

DATABASE = "works.db"

def get_db_connection():
    """
    Create and return a database connection.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
@app.route("/dashboard")
def dashboard():
    """
    Display dashboard with registered works.
    """
    conn = get_db_connection()
    works = conn.execute("SELECT * FROM works").fetchall()
    conn.close()

    return render_template("dashboard.html", works=works)


@app.route("/works/create", methods=["GET", "POST"])
def create_work():
    """
    Create a new construction work.
    """
    error = None

    if request.method == "POST":
        name = request.form.get("name")
        client = request.form.get("client")
        start_date = request.form.get("start_date")
        status = request.form.get("status")

        if not name or not client:
            error = "Work name and client are required"
        else:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO works (name, client, start_date, status) VALUES (?, ?, ?, ?)",
                (name, client, start_date, status),
            )
            conn.commit()
            conn.close()

        flash("Work created successfully!")
        return redirect(url_for("dashboard"))

    return render_template("work_create.html", error=error)
@app.route("/works/<int:id>/edit", methods=["GET", "POST"])
def edit_work(id):
    """
    Edit an existing work.
    """
    conn = get_db_connection()
    work = conn.execute("SELECT * FROM works WHERE id = ?", (id,)).fetchone()

    if work is None:
        conn.close()
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        name = request.form.get("name")
        client = request.form.get("client")
        start_date = request.form.get("start_date")
        status = request.form.get("status")

        if not name or not client:
            conn.close()
            return render_template("work_edit.html", work=work, error="Name and client are required")

        conn.execute(
            """
            UPDATE works
            SET name = ?, client = ?, start_date = ?, status = ?
            WHERE id = ?
            """,
            (name, client, start_date, status, id),
        )
        conn.commit()
        conn.close()

        flash("Work updated successfully!")
        return redirect(url_for("dashboard"))


    conn.close()
    return render_template("work_edit.html", work=work)

@app.route("/works/<int:id>/delete", methods=["POST"])
def delete_work(id):
    """
    Delete a work.
    """
    conn = get_db_connection()
    conn.execute("DELETE FROM works WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    flash("Work deleted successfully!")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
