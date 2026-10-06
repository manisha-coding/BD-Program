#Improve this Flask Shopping Cart API. Keep the existing
#/addOrders and /showOrders endpoints. Improve the JSON 
# response format by adding proper HTTP status codes, 
# success/failure status, meaningful messages, and a 
# structured response. Also add validation for missing 
# product, quantity, and price.

from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/addOrders', methods=['POST'])
def add_order():

    data = request.get_json()

    # Check whether all required fields are present
    if not data:
        return jsonify({
            "success": False,
            "status": 400,
            "message": "Request body is required",
            "data": None
        }), 400

    if "product" not in data or "quantity" not in data or "price" not in data:
        return jsonify({
            "success": False,
            "status": 400,
            "message": "Product, quantity and price are required",
            "data": None
        }), 400

    # Create order
    order = {
        "id": len(orders) + 1,
        "product": data["product"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    orders.append(order)

    return jsonify({
        "success": True,
        "status": 201,
        "message": "Order added successfully",
        "data": order
    }), 201


# Show Orders
@app.route('/showOrders', methods=['GET'])
def show_orders():

    if len(orders) == 0:
        return jsonify({
            "success": False,
            "status": 404,
            "message": "No orders found",
            "data": []
        }), 404

    return jsonify({
        "success": True,
        "status": 200,
        "message": "Orders retrieved successfully",
        "count": len(orders),
        "data": orders
    }), 200


if __name__ == '__main__':
    app.run(debug=True)