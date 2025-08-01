from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from pymongo import MongoClient
import json
import os
from datetime import datetime


app = Flask(__name__)
app.secret_key = 'assignment_secret_key'

# Local MongoDB connection string
MONGODB_URI = "mongodb://localhost:27017"

# Function to read data from the backend file
def get_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading data file: {e}")
        # Return fallback data if file can't be read
        return [
            {"id": 1, "name": "Fallback Data", "email": "fallback@example.com"}
        ]

@app.route('/api')
def api():
    return jsonify(get_data())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Connect to MongoDB Atlas and insert data
        client = MongoClient(MONGODB_URI)
        db = client['myapp_db']
        collection = db['user_data']
        collection.insert_one(data)
        
        # Redirect to success page
        return redirect(url_for('success'))
    except Exception as e:
        # Display error on the same page without redirection
        error_message = f"Error: {str(e)}"
        return render_template('index.html', error=error_message)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        # Get form data
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')
        
        # Connect to MongoDB and insert data
        client = MongoClient(MONGODB_URI)
        db = client['myapp_db']
        todo_collection = db['todo_items']
        
        # Create document to insert
        todo_item = {
            'itemName': item_name,
            'itemDescription': item_description,
            'createdAt': datetime.now()
        }
        
        # Insert into MongoDB
        todo_collection.insert_one(todo_item)
        
        # Redirect to success page
        return redirect(url_for('success'))
    except Exception as e:
        # Display error on the same page without redirection
        error_message = f"Error: {str(e)}"
        return render_template('todo.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
