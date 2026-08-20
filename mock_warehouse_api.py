from flask import Flask, jsonify
import random

app = Flask(__name__)

# Simulated warehouse inventory
INVENTORY = {
    "SKU-1001": 42,
    "SKU-1002": 17,
    "SKU-1003": 88
}

@app.route('/warehouse/stock')
def get_stock():
    # Simulate stock fluctuating slightly each poll, like a reall warehouse
    for sku in INVENTORY:
        INVENTORY[sku] += random.randint(-2, 2)
        INVENTORY[sku] = max(0, INVENTORY[sku])
    return jsonify(INVENTORY)

if __name__ == '__main__':
    app.run(port=5001, debug=True)