from flask import Blueprint, jsonify
from .models import data_store
from .services import process_data

main = Blueprint('main', __name__)

mock_data = {
    'items': [
        {'id': 1, 'name': 'iTem1', 'value': 100},
        {'id': 2, 'name': 'itEm2', 'value': 48},
        {'id': 3, 'name': 'iteM3', 'value': 36}
    ]
}

@main.route('/fetch-data', methods=['GET'])
def fetch_data():
    """Fetch data from a simulated external service."""
    data_store['fetched_data'] = mock_data
    data_store['processed_data'] = process_data(mock_data)
    return jsonify(data_store['fetched_data']), 200

@main.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """Retrieve processed data."""
    return jsonify(data_store['processed_data']), 200
