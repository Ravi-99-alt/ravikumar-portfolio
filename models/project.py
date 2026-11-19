
from models import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    title = db.Column(
        db.String(120),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    tech_stack = db.Column(
        db.String(255),
        nullable=False
    )

    image = db.Column(
        db.String(255),
        nullable=True
    )

    github_url = db.Column(
        db.String(255),
        nullable=True
    )

    live_url = db.Column(
        db.String(255),
        nullable=True
    )

    featured = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )

    def __repr__(self):
        return f"<Project {self.title}>"
