NavisWebhost Satellite Data Dashboard

The NavisWebhost Satellite Data Dashboard is an interactive, real-time web interface designed to monitor and visualize live satellite telemetry and environmental data. Built with Flask for the backend and Tailwind CSS for responsive frontend design, this dashboard offers an intuitive and visually appealing way to track critical satellite parameters, motion data, environmental conditions, and system health.

Key Features:

Real-Time Telemetry & Environmental Data

Temperature: Monitors the current ambient temperature of the satellite payload in Celsius.

Pressure: Displays atmospheric pressure (hPa) as detected by onboard sensors.

Altitude: Tracks the satellite’s current altitude in meters relative to a reference point.

Motion & Orientation: Shows acceleration across X, Y, and Z axes, as well as orientation (pitch, yaw, roll) for precise satellite positioning.

System Health Monitoring

Battery Level: Provides current battery percentage to ensure continuous operation.

Satellites Connected: Displays the number of connected satellites for networked constellations.

Air Quality Index (AQI) & Toxic Gas Detection: Monitors onboard environmental conditions including CO₂, CO, and NO₂ levels.

UV Detection & Alerts: Tracks UV exposure and anomaly alerts for proactive response.

Live Location and Time

Displays Latitude and Longitude coordinates for real-time satellite positioning.

IST Date & Time: Automatically updates according to Indian Standard Time using client-side JavaScript.

Satellite Webcam Footage Placeholder

A dedicated section for live video streaming from the satellite or connected camera systems.

Supports integration with OpenCV or other ML-based object detection systems to monitor live visuals and detect anomalies.

Visual Status Indicators

A color-coded system status indicator provides an immediate overview of operational health.

Green: Normal operation

Yellow: Minor anomalies or warnings

Red (future expansion): Critical issues

Modern, Responsive Design

Uses Tailwind CSS for a fully responsive layout optimized for desktops, tablets, and mobile devices.

Dark theme with clean typography and card-based data display ensures readability and accessibility.

Backend Simulation

Powered by a Flask Python backend, the dashboard currently uses mock data generation for telemetry, sensor, and system information, simulating real satellite operations.

Real-time data updating is achieved via JavaScript for live clocks, with future potential for WebSocket or AJAX integration for continuous telemetry streaming.

Technical Stack

Frontend: HTML5, Tailwind CSS, JavaScript

Backend: Python Flask

Data Simulation: Randomized satellite telemetry and environmental readings

Deployment: Render.com compatible, supports cloud hosting

This dashboard is ideal for satellite operators, researchers, and enthusiasts who need an accessible, visually informative platform to monitor real-time satellite health, location, and environmental conditions. Future enhancements can include live telemetry streaming, ML-based object detection, and advanced analytics for predictive satellite operations.
