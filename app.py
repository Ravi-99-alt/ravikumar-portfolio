
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)

from sqlalchemy import text

from config import Config
from models import db
from models.project import Project
from models.skill import Skill
from models.message import Message


# Initialize Flask application
app = Flask(__name__)

# Load application configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)


# Homepage
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message_text = request.form.get("message", "").strip()

        # Validate required fields
        if not name or not email or not message_text:
            flash("Please fill in all required fields.", "error")
            return redirect(url_for("home") + "#contact")

        # Validate field lengths
        if (
            len(name) > 100
            or len(email) > 150
            or len(subject) > 180
        ):
            flash("Please check the length of your input.", "error")
            return redirect(url_for("home") + "#contact")

        try:
            new_message = Message(
                name=name,
                email=email,
                subject=subject or None,
                message=message_text
            )

            db.session.add(new_message)
            db.session.commit()

            flash(
                "Your message was sent successfully!",
                "success"
            )

        except Exception:
            db.session.rollback()

            app.logger.exception(
                "Unable to save contact message"
            )

            flash(
                "Something went wrong. Please try again.",
                "error"
            )

        return redirect(url_for("home") + "#contact")

    # Retrieve projects from MySQL
    projects = Project.query.order_by(
        Project.id.desc()
    ).all()

    # Retrieve skills from MySQL
    skills = Skill.query.order_by(
        Skill.skill_name.asc()
    ).all()

    return render_template(
        "index.html",
        projects=projects,
        skills=skills
    )


# Database connection test
@app.route("/health")
def health():

    try:
        db.session.execute(text("SELECT 1"))

        return jsonify({
            "status": "success",
            "database": "connected"
        }), 200

    except Exception:
        db.session.rollback()

        app.logger.exception(
            "Database health check failed"
        )

        return jsonify({
            "status": "error",
            "database": "not connected"
        }), 500


# Custom 404 page
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404


# Run Flask application
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
