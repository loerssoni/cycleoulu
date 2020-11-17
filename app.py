# app.py
from flask import Flask
from flask import render_template
from Database import db, PublicServices
from flask_sqlalchemy import SQLAlchemy
from data.traffic_announcements import get_traffic_announcements
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./data/oukadata.db'
db.init_app(app)

@app.route("/")
def traffic():
    data = get_traffic_announcements()
    geojson = [i['geojson'] for i in data]
    geojson = json.dumps(geojson)
    descriptions = [i['descriptions'] for i in data]
    descriptions = json.dumps(descriptions)
    print(descriptions)
    template =  render_template("layout.html", geodata = geojson,
            descriptions = descriptions)
    return template


if __name__ == '__main__':
    app.run(debug=True)