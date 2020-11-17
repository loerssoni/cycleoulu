from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PublicServices(db.Model):
    __tablename__ = 'oukaJulkiset'
    __table_args__ = { 'extend_existing': True }
    index = db.Column(db.Text, primary_key=True)

