import flask
app = flask.Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return '''<h1>Swift Post API</h1>
    <hr>
    <p>This is the Application Programming Interface for the iOS application (SwiftPost) which is an application for tracking packages from multiple delivery services such as Canada Post, FedEX, UPS, Purolator, DHL, etc.</p>
    <p>This API makes use of the <a href="https://www.easypost.com/docs/api">easypost</a> which suppliers Shipping API, Tracking API, and Address Verification API for USPS, FedEx, UPS, DHL, and many more. This API is in its development stage.</p>'''
