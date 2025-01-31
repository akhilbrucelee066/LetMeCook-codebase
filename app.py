from flask import Flask, render_template, request, jsonify, session, redirect
from model_res import generate_recipe

app = Flask(__name__)
app.secret_key = 'letmecook123'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_recipe", methods=["POST"])
def create_recipe():
    try:
        data = request.json
        recipe = generate_recipe(data)
        session['recipe'] = recipe
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/recipe")
def show_recipe():
    recipe = session.get('recipe')
    return render_template("recipe.html", recipe=recipe)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)