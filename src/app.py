from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    button_id = db.Column(db.String(50), nullable=False)
    sequence_num = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(10), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click', methods=['POST'])
def register_click():
    data = request.json
    button_id = data.get('button_id')
    
    now = datetime.now()
    today = now.date()
    current_time = now.strftime("%H:%M")
    
    # Get last sequence number for today
    last_click = Click.query.filter_by(date=today).order_by(Click.sequence_num.desc()).first()
    new_sequence = (last_click.sequence_num + 1) if last_click else 1
    
    new_click = Click(
        button_id=button_id,
        sequence_num=new_sequence,
        date=today,
        time=current_time
    )
    db.session.add(new_click)
    db.session.commit()
    
    return jsonify({
        'status': 'success',
        'sequence': new_sequence,
        'date': today.strftime("%Y-%m-%d"),
        'time': current_time
    })

@app.route('/stats')
def get_stats():
    today = datetime.now().date()
    clicks = Click.query.filter_by(date=today).all()
    
    stats = {
        'total': len(clicks),
        'buttons': {
            'Botao 1': 0,
            'Botao 2': 0,
            'Botao 3': 0,
            'Botao 4': 0
        }
    }
    
    for click in clicks:
        if click.button_id in stats['buttons']:
            stats['buttons'][click.button_id] += 1
            
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
