# Spam Email Detection Project

This project implements a machine learning model to detect spam emails.

## Project Structure

- `app.py`: Flask application to serve the model.
- `spam_data.csv`: Dataset used for training and testing the model.
- `spam_detection.py`: Contains the machine learning model training and prediction logic.
- `static/style.css`: CSS file for styling the web interface.
- `templates/index.html`: HTML template for the web interface.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd "Spam email detection project"
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   ./venv/Scripts/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000` to access the spam email detection interface.

## Model Details

The `spam_detection.py` script trains a machine learning model (e.g., Naive Bayes, SVM) on the `spam_data.csv` dataset to classify emails as spam or not spam.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
