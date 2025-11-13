import os
import base64
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from werkzeug.utils import secure_filename
from helpers import apology, allowed_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'outfitmaker'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

db = SQL("sqlite:///outfits.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Show outfit maker"""
    categories = ['upper', 'lower', 'shoes', 'accessories']
    items_by_category = {}

    for category in categories:
        items = db.execute(
            "SELECT * FROM clothing_items WHERE category = ?",
            category
        )
        for item in items:
            if item['image_path'].startswith('static/'):
                item['image_path'] = item['image_path'][7:]
        items_by_category[category] = items

    outfits = db.execute("SELECT * FROM outfits")

    return render_template("index.html",
                         items_by_category=items_by_category,
                         categories=categories,
                         outfits=outfits)

@app.route("/upload", methods=["POST"])
def upload():
    """Upload clothing item"""
    if 'file' not in request.files:
        return apology("No file selected", 400)

    file = request.files['file']
    category = request.form.get("category", "upper")
    name = request.form.get("name", "Unnamed Item")

    if file.filename == '':
        return apology("No file selected", 400)

    if file and allowed_file(file.filename):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        relative_path = filepath.replace('static/', '')

        db.execute(
            "INSERT INTO clothing_items (name, category, image_path) VALUES (?, ?, ?)",
            name, category, relative_path
        )

        flash("Item uploaded successfully!")
        return redirect("/")

    return apology("Invalid file type", 400)

@app.route("/save_outfit", methods=["POST"])
def save_outfit():
    """Save current outfit with canvas screenshot"""
    name = request.form.get("name")
    canvas_image = request.form.get("canvas_image", "")

    if not name:
        return apology("Outfit name is required", 400)

    db.execute("INSERT INTO outfits (name, canvas_image) VALUES (?, ?)", name, canvas_image)
    flash("Outfit saved successfully!")
    return redirect("/")

@app.route("/delete_outfit/<int:outfit_id>", methods=["POST"])
def delete_outfit(outfit_id):
    """Delete saved outfit"""
    db.execute("DELETE FROM outfits WHERE id = ?", outfit_id)
    flash("Outfit deleted!")
    return redirect("/")

@app.route("/delete_all_items", methods=["POST"])
def delete_all_items():
    """Delete all items uploaded"""
    try:
        item_count = db.execute("SELECT COUNT(*) as count FROM clothing_items")[0]['count']
        db.execute("DELETE FROM clothing_items")
        flash(f"ALL {item_count} items deleted successfully!")
    except Exception as e:
        flash("Error deleting items!")
        print(f"Error: {e}")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
