import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values('../.env')
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__,
    template_folder='templates'
)

# Index route
@app.route("/")
def index():
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"user", "content": "Give me the name of a U.S. president: "
            }
        ]
    )

    return response.choices[0].message.content
    #return render_template("index.html")

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    return "Testing flask routes"

if __name__=="__main__":
    app.run(debug=True)