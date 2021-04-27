import flask
#import easypost

app = flask.Flask(__name__)
app.config["DEBUG"] = True
#easypost.api_key = "EZAK2b2b7bf3cfcb44bbaa40f92ce17cefd4weXKTMo9e7JFSyG3kj2T3g"

@app.route("/")
def home():
    return '''<h1>Swift Post API</h1>
    <hr>
    <p>This is the Application Programming Interface for the iOS application (SwiftPost) which is an application for tracking packages from multiple delivery services such as Canada Post, FedEX, UPS, Purolator, DHL, etc.</p>
    <p>This API makes use of the <a href="https://www.easypost.com/docs/api">easypost</a> which suppliers Shipping API, Tracking API, and Address Verification API for USPS, FedEx, UPS, DHL, and many more. This API is in its development stage.</p>'''

#@app.route('/dev/v1/resources/track_shipment', methods=['GET'])
#def retrieveTrackingData():
#    tracking_code = flask.request.args.get('tracking_code')
#    carrier = flask.request.args.get('carrier')
#    tracking_data = easypost.Tracker.create(tracking_code = tracking_code, carrier = carrier)
#
#    temp = [tracking_data.to_dict()]
#    return flask.jsonify(temp)
    
#app.run()
