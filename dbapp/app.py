from flask import Flask, jsonify, request
from waitress import serve
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Predict(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sl = db.Column(db.Float)
    sw = db.Column(db.Float)
    pl = db.Column(db.Float)
    pw = db.Column(db.Float)
    prediction = db.Column(db.String(50))

@app.route('/records', methods=['GET', 'POST'])
def record():
    if request.method == 'GET':
        records = Predict.query.all()
        return jsonify([{"id": r.id, "sl": r.sl, "sw": r.sw, "pl": r.pl, "pw": r.pw, "prediction": r.prediction} for r in records])

    else:
        record = request.get_json()
        record = Predict(**record)
        db.session.add(record)
        db.session.commit()
        return jsonify({"message": "Record added successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    serve(app, host="0.0.0.0", port="5001")