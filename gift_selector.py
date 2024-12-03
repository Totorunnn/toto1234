from flask import Flask, request, render_template_string

app = Flask(__name__)

gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones", "Smartphone",
    "Laptop", "Watch", "Shoes", "Wallet", "Headset", "Camera",
    "Drone", "Smart Watch", "Bluetooth Speaker"
]

@app.route('/')
def gift_selection():
    return render_template_string('''
        <h1>Available Gifts</h1>
        <ul>
        {% for index, gift in enumerate(gifts) %}
            <li>{{ index }}: {{ gift }}</li>
        {% endfor %}
        </ul>
        <form action="/result" method="get">
            <label for="selection">Enter gift indices (comma-separated):</label>
            <input type="text" name="selection" id="selection">
            <button type="submit">Submit</button>
        </form>
    ''', gifts=gifts)

@app.route('/result')
def result():
    indices = request.args.get('selection', '').split(',')
    try:
        indices = list(map(int, indices))
        selected_gifts = [gifts[i] for i in indices]
        gift_code = 0
        for index in indices:
            gift_code |= (1 << index)
        return render_template_string('''
            <h1>Gift Selection Result</h1>
            <p>Selected Gifts: {{ selected_gifts }}</p>
            <p>Unique Gift Code: {{ gift_code }}</p>
            <a href="/">Go back</a>
        ''', selected_gifts=selected_gifts, gift_code=gift_code)
    except:
        return "Invalid input. Please use valid indices."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
