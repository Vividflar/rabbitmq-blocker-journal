from flask import Flask, jsonify
import requests
import threading
import time

app = Flask(__name__)

# The chache
stock_cache = {}

def poll_warehouse():
    """Runs forever in a background thread, polling every 5 minutes."""
    while True:
        try:
            response = requests.get('http://localhost:5001/warehouse/stock')
            response.raise_for_status()
            global stock_cache
            stock_cache = response.json()
            print(f"[poller] Cache update: {stock_cache}")
        except requests.RequestException as e:
            print(f"[poller] Failed to poll warehouse API: {e}")
        time.sleep(300)  # 5 minutes
        
@app.route('/stock/<product_id>')
def get_stock(product_id):
    quantity = stock_cache.get(product_id)
    if quantity is None:
        return jsonify({"error": "product not found"}), 404
    return jsonify({"product_id": product_id, "quantity": quantity})

@app.route('/stock')
def get_all_stock():
    return jsonify(stock_cache)

if __name__ == '__main__':
    # Do one poll immediately on startup so the cache isn't empty
    poll_warehouse_thread = threading.Thread(target=poll_warehouse, daemon=True)
    poll_warehouse_thread.start()
    app.run(port=5000, debug=True, use_reloader=False)
        