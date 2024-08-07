def process_data(data):
    """Process the fetched data (this example is for converting names to uppercase)."""
    if not data or 'items' not in data:
        return None
    processed = [
        {'id': item['id'], 'name': item['name'].upper(), 'value': item['value']}
        for item in data['items']
    ]
    return processed
