# Flask MongoDB Application

A simple Flask application that demonstrates API integration and form submission with MongoDB Atlas.

## Features

- RESTful API endpoint returning JSON data
- MongoDB Atlas integration for data storage
- Form submission with success/error handling
- Clean and responsive frontend design

## Setup Instructions

1. Install Python 3.7 or higher
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your MongoDB Atlas connection string:
   ```
   MONGODB_URI=your_mongodb_atlas_connection_string
   ```
4. Run the application:
   ```
   python app.py
   ```

## API Endpoints

- `GET /api`: Returns a JSON list of sample data
- `GET /`: Main page with form
- `POST /submit`: Endpoint for form submission
- `GET /success`: Success page after successful submission

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── templates/          # HTML templates
│   ├── index.html     # Main form page
│   └── success.html   # Success page
└── static/            # Static assets
```

## Error Handling

- Form submissions are validated
- MongoDB connection errors are caught and displayed
- API errors are gracefully handled

## MongoDB Integration

- Uses MongoDB Atlas for cloud database
- Data is stored in 'myapp_db' database
- Collection name: 'user_data'

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License
