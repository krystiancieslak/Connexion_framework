from flask import Flask
import connexion


app = connexion.App(__name__)
app.add_api('my_api.yaml')
app.run(port=5001)

@app.route("/")
def home():
    return "hello there"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.add_api("my_api.yaml")
    app.run(host='0.0.0.0')