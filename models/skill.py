
from models import db


class Skill(db.Model):
    __tablename__ = "skills"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    skill_name = db.Column(
        db.String(100),
        nullable=False
    )

    category = db.Column(
        db.String(100),
        nullable=True
    )

    proficiency = db.Column(
        db.Integer,
        default=70,
        nullable=True
    )

    def __repr__(self):
        return f"<Skill {self.skill_name}>"
