from .database import db
from sqlalchemy import String, Integer, Column

class Product(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True, nullable=False)
    info = Column(
        String(25),
        nullable=False,
        default="",
        server_default="",
    )