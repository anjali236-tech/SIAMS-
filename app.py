from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# ---------- MySQL Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flask_user",
        password="password123",
        database="asset_management",
        charset="utf8"
    )

# ---------- Counts ----------
def get_asset_counts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) as total FROM assets")
    total = cursor.fetchone()['total'] or 0
    cursor.execute("SELECT COUNT(*) as issued FROM assets WHERE status='issued'")
    issued = cursor.fetchone()['issued'] or 0
    cursor.execute("SELECT COUNT(*) as maintenance FROM assets WHERE status='maintenance'")
    maintenance = cursor.fetchone()['maintenance'] or 0
    conn.close()
    return total, issued, maintenance

# ---------- Dashboard ----------
@app.route('/')
def dashboard():
    total_assets, issued_assets, maintenance_assets = get_asset_counts()
    return render_template(
        "dashboard.html",
        total_assets=total_assets,
        issued_assets=issued_assets,
        maintenance_assets=maintenance_assets,
        search_result=None,
        all_assets=None
    )

# ---------- Add Asset ----------
@app.route("/add_asset", methods=["POST"])
def add_asset():
    name = request.form.get("asset_name")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assets (name, status) VALUES (%s, %s)", (name, "available"))
    conn.commit()
    conn.close()
    flash(f"Asset '{name}' added successfully!", "success")
    return redirect(url_for("dashboard"))

# ---------- Issue Asset ----------
@app.route("/issue", methods=["POST"])
def issue_asset():
    name = request.form.get("asset_name")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE assets SET status='issued' WHERE name=%s", (name,))
    conn.commit()
    conn.close()
    flash(f"Asset '{name}' issued successfully!", "success")
    return redirect(url_for("dashboard"))

# ---------- Return Asset ----------
@app.route("/return_asset", methods=["POST"])
def return_asset():
    name = request.form.get("asset_name")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE assets SET status='available' WHERE name=%s AND status='issued'", (name,))
    if cursor.rowcount > 0:
        flash(f"Asset '{name}' returned successfully!", "success")
    else:
        flash(f"Asset '{name}' was not issued or does not exist.", "error")
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

# ---------- Send to Maintenance ----------
@app.route("/maintenance", methods=["POST"])
def maintenance_asset():
    name = request.form.get("asset_name")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE assets SET status='maintenance' WHERE name=%s", (name,))
    conn.commit()
    conn.close()
    flash(f"Asset '{name}' sent to maintenance!", "success")
    return redirect(url_for("dashboard"))

# ---------- Search Asset ----------
@app.route("/search", methods=["POST"])
def search_asset():
    keyword = request.form.get("search_keyword")
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM assets WHERE name LIKE %s", ('%' + keyword + '%',))
    assets = cursor.fetchall()
    conn.close()

    message = f"Found: {assets[0]['name']} (Status: {assets[0]['status']})" if assets else "Asset not found"
    total_assets, issued_assets, maintenance_assets = get_asset_counts()
    return render_template(
        "dashboard.html",
        search_result=message,
        all_assets=None,
        total_assets=total_assets,
        issued_assets=issued_assets,
        maintenance_assets=maintenance_assets
    )

# ---------- Show All ----------
@app.route("/show_all", methods=["GET"])
def show_all_assets():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM assets")
    assets = cursor.fetchall()
    conn.close()

    total_assets, issued_assets, maintenance_assets = get_asset_counts()
    return render_template(
        "dashboard.html",
        all_assets=assets,
        search_result=None,
        total_assets=total_assets,
        issued_assets=issued_assets,
        maintenance_assets=maintenance_assets
    )

# ---------- Close Table ----------
@app.route("/close_table", methods=["POST"])
def close_table():
    total_assets, issued_assets, maintenance_assets = get_asset_counts()
    return render_template(
        "dashboard.html",
        all_assets=None,
        search_result=None,
        total_assets=total_assets,
        issued_assets=issued_assets,
        maintenance_assets=maintenance_assets
    )

if __name__ == "__main__":
    app.run(debug=True)
