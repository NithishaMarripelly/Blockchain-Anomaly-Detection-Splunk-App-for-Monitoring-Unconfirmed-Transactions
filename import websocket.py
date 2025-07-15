import websocket
import json
import requests
import time

# Splunk HEC details
SPLUNK_HEC_URL = "https://127.0.0.1:8088/services/collector"
SPLUNK_HEC_TOKEN = "40436211-2399-4a81-a954-98fddb07d2c2"

# Function to send data to Splunk
def send_to_splunk(data):
    headers = {
        "Authorization": f"Splunk {SPLUNK_HEC_TOKEN}"
    }
    payload = {
        "event": data,
        "sourcetype": "bitcoin_transaction"
    }
    response = requests.post(SPLUNK_HEC_URL, headers=headers, json=payload, verify=False)
    if response.status_code != 200:
        print(f"Failed to send data to Splunk: {response.text}")

# WebSocket message handler
def on_message(ws, message):
    transaction = json.loads(message)

    # Extract only selected fields
    try:
        extracted_data = {
            "hash": transaction.get("x", {}).get("hash"),
            "time": transaction.get("x", {}).get("time"),
            "input_address": transaction.get("x", {}).get("inputs", [{}])[0].get("prev_out", {}).get("addr"),
            "input_value": transaction.get("x", {}).get("inputs", [{}])[0].get("prev_out", {}).get("value"),
            "output_address": transaction.get("x", {}).get("out", [{}])[0].get("addr"),
            "output_value": transaction.get("x", {}).get("out", [{}])[0].get("value"),
            "size": transaction.get("x", {}).get("size"),
            "relayed_by": transaction.get("x", {}).get("relayed_by")
        }

        # Send filtered data to Splunk
        send_to_splunk(extracted_data)

    except Exception as e:
        print(f"Error parsing message: {e}")

# WebSocket event handlers
def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket connection closed")

def on_open(ws):
    # Subscribe to unconfirmed transactions
    ws.send(json.dumps({"op": "unconfirmed_sub"}))

# Main function to start the WebSocket connection
if __name__ == "__main__":
    websocket_url = "wss://ws.blockchain.info/inv"
    ws = websocket.WebSocketApp(
        websocket_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever()
