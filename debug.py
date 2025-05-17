from flask import Flask, request, jsonify
from customer import Customer
from coffee import Coffee
from order import Order

app = Flask(__name__)

# Mock in-memory data store
customers = []
coffees = []
orders = []

@app.route("/")
def home():
    return "Welcome to the Coffee Shop API!"

@app.route("/customers", methods=["POST"])
def create_customer():
    name = request.json.get("name")
    try:
        customer = Customer(name)
        customers.append(customer)
        return jsonify({"message": f"Customer {name} created."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/coffees", methods=["POST"])
def create_coffee():
    name = request.json.get("name")
    try:
        coffee = Coffee(name)
        coffees.append(coffee)
        return jsonify({"message": f"Coffee {name} created."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/orders", methods=["POST"])
def create_order():
    customer_name = request.json.get("customer")
    coffee_name = request.json.get("coffee")
    price = float(request.json.get("price"))

    customer = next((c for c in customers if c.name == customer_name), None)
    coffee = next((c for c in coffees if c.name == coffee_name), None)

    if not customer or not coffee:
        return jsonify({"error": "Customer or coffee not found"}), 404

    try:
        order = customer.create_order(coffee, price)
        orders.append(order)
        return jsonify({"message": "Order created."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/customers/<name>/coffees")
def get_customer_coffees(name):
    customer = next((c for c in customers if c.name == name), None)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404
    return jsonify([coffee.name for coffee in customer.coffees()])

if __name__ == "__main__":
    app.run(debug=True)
