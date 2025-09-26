from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/move', methods=['GET', 'POST'])
def handle_move():
    """
    Handles both GET and POST requests to the /move endpoint.
    It logs the request details and returns a success response.
    """
    if request.method == 'GET':
        direction = request.args.get('direction', 'Unknown')
        print(f"--- Received GET Request ---")
        print(f"Endpoint: /move")
        print(f"Query Parameter 'direction': {direction}")

        return jsonify({
            "status": "success",
            "message": f"GET command received for direction: {direction}",
            "method": "GET"
        }), 200

    elif request.method == 'POST':
        try:
            data = request.get_json(silent=True)
            if not data:
                return jsonify({"status": "error", "message": "Invalid JSON body"}), 400

            command = data.get('command', 'N/A')
            direction = data.get('direction', 'Unknown')

            print(f"--- Received POST Request ---")
            print(f"Endpoint: /move")
            print(f"JSON Payload: {data}")
            print(f"Command: {command}, Direction: {direction}")

            return jsonify({
                "status": "success",
                "message": f"POST command received for direction: {direction}",
                "method": "POST"
            }), 200

        except Exception as e:
            print(f"Error processing POST request: {e}")
            return jsonify({"status": "error", "message": f"Internal server error: {str(e)}"}), 500


if __name__ == '__main__':
    # i believe http://127.0.0.1:5000 is the link on which it will run
    print("Starting Flask Mock API Server on http://127.0.0.1:5000/...")
    app.run(debug=True)
