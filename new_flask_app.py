import connexion
import os

app = connexion.App(__name__)

@app.route("/")
def home():
    return "hello there"

if __name__ == "__main__":
    app.add_api('my_api.yaml')
    port = int(os.environ.get('PORT', 5001))
    app.run(port=5001, host='0.0.0.0')