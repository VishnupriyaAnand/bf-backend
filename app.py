from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the BFHL API!", 200

# GET Endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# POST Endpoint
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get("data", [])
        if not data or not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input data"}), 400

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lower_case_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lower_case_alphabets) if lower_case_alphabets else None

        user_id = "VishnupriyaAnand"  # Replace with your dynamic user ID logic
        email = "vishnupriya.anand03@gmail.com"
        roll_number = "21BCB0042"

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
