from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Soru(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    soru_metni = db.Column(db.String(200), nullable=False)
    dogru_cevap = db.Column(db.String(100), nullable=False)

