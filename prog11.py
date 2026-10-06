from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/addOrders', methods=['POST'])
def add_order():

    data = request.get_json()

    order = {
        "product": data["product"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    orders.append(order)

    return jsonify({
        "message": "Order added successfully",
        "order": order
    }), 201


# Endpoint to show recent orders
@app.route('/showOrders', methods=['GET'])
def show_orders():

    return jsonify({
        "message": "Recent orders",
        "orders": orders
    })


if __name__ == '__main__':
    app.run(debug=True)