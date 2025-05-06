from flask import Flask, send_from_directory
from api import create_app

app = create_app()  # Initialize the Flask app with the Blueprint

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')  # Serve frontend

if __name__ == "__main__":
    
 port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port, debug=True)

