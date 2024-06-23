from flask import Flask, render_template, request

app = Flask(__name__,
    template_folder='templates'
)

# Index route
@app.route("/")
def index():
    return "First Flask Program!"

@app.route("/test")
def test():
    return "Testing flask routes"

if __name__=="__main__":
    app.run(debug=True)