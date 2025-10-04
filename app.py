import datetime
import random
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

def generate_mock_data():
    """Generates a dictionary of mock satellite data for the dashboard."""
    # Data is simulated to look realistic for a satellite payload/sensor array
    data = {
        # Core Environmental Data
        'temperature': round(random.uniform(-10.0, 35.0), 2),  # Celsius
        'pressure': round(random.uniform(980.0, 1030.0), 2),    # hPA
        'altitude': round(random.uniform(300.0, 800.0), 2),     # meters (relative to a base)

        # Motion and Orientation Data (e.g., from an IMU)
        'accel_x': round(random.uniform(-0.5, 0.5), 2),
        'accel_y': round(random.uniform(-0.5, 0.5), 2),
        'accel_z': round(random.uniform(9.7, 9.9), 2), # Gravity
        'orient_x': round(random.uniform(0.0, 360.0), 1),
        'orient_y': round(random.uniform(0.0, 360.0), 1),
        'orient_z': round(random.uniform(0.0, 360.0), 1),

        # Location and Time (IST - Indian Standard Time)
        'latitude': round(random.uniform(48.0, 49.0), 4),
        'longitude': round(random.uniform(77.0, 78.0), 4),
        'ist_date': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%d/%m/%Y'),
        'ist_time': datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%H:%M:%S'),

        # Status and System Data
        'aqi': random.randint(20, 150),
        'alert_sent': random.choice(['No', 'Minor Anomaly']),
        'satellites_connected': random.randint(8, 24),
        'uv_detection': random.choice(['Yes', 'No']),
        'uv_count': random.randint(0, 5),
        'battery_level': random.randint(60, 100), # Percentage

        # Toxic Gas Levels (e.g., parts per million or similar scale)
        'gas_co2': random.randint(400, 500), # PPM
        'gas_no2': round(random.uniform(0.01, 0.1), 2),
        'gas_co': round(random.uniform(0.5, 5.0), 1)
    }

    # Set status for visual feedback
    data['status_color'] = 'bg-green-500' if data['alert_sent'] == 'No' and data['battery_level'] > 70 else 'bg-yellow-500'

    return data

@app.route('/')
def dashboard():
    """Renders the main dashboard page with generated data."""
    data = generate_mock_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Setting debug=True allows the server to automatically reload on code changes
    # and provides helpful error messages.
    app.run(debug=True)
