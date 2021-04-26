import easypost
import flask
from flask import request, jsonify

easypost.api_key = "EZAK2b2b7bf3cfcb44bbaa40f92ce17cefd4weXKTMo9e7JFSyG3kj2T3g"
app = flask.Flask(__name__)
#app.config["DEBUG"] = True

to_address = easypost.Address.create(
    name = 'Dr. Steve Brule',
    street1 = '179 N Harbor Dr',
    city = 'Redondo Beach',
    state = 'CA',
    zip = '90277',
    country = 'US',
    phone = '4153334444',
    email = 'dr_steve_brule@gmail.com')

from_address = easypost.Address.create(
    street1 = "417 Montgomery Street",
    street2 = "FLOOR 5",
    city = "San Francisco",
    state = "CA",
    zip = "94104",
    country = "US",
    company = "EasyPost",
    phone = "415-456-7890")

parcel = easypost.Parcel.create(
    length = 20.2,
    width = 10.9,
    height = 5,
    weight = 65.9)

customs_info = easypost.CustomsInfo.create(
    eel_pfc = 'NOEEI 30.37(a)',
    customs_certify = True,
    customs_signer = 'Steve Brule',
    contents_type = 'merchandise',
    contents_explanation = '',
    restriction_type = 'none',
    restriction_comments = '',
    non_delivery_option = 'abandon',
    customs_items = [{
        'description': 'Sweet shirts',
        'quantity': 2,
        'weight': 11,
        'value': 23,
        'hs_tariff_number': '654321',
        'origin_country': 'US'}])


@app.route('/', methods=['GET'])
def home():
    return
    '''<h1>Swift Post API</h1>
    <hr>
    <p>This is the Application Programming Interface for the iOS application (SwiftPost) which is an application for tracking packages from multiple delivery services such as Canada Post, FedEX, UPS, Purolator, DHL, etc. This API makes use of the <a href="https://www.easypost.com/docs/api">easypost</a> which suppliers Shipping API, Tracking API, and Address Verification API for USPS, FedEx, UPS, DHL, and many more. This API is in its development stage.</p>'''


@app.route('/dev/api/v1/resources/parcel', methods=['GET'])
def getParcelData():
    shipment = easypost.Shipment.create(
    to_address = to_address,
    from_address = from_address,
    parcel = parcel,
    customs_info = customs_info)
    
    temp = [shipment.parcel.to_dict()]
    return jsonify(temp)
    
    
@app.route('/dev/api/v1/resources/from_address', methods=['GET'])
def getFromAddressData():
    shipment = easypost.Shipment.create(
    to_address = to_address,
    from_address = from_address,
    parcel = parcel,
    customs_info = customs_info)
    
    temp = [shipment.from_address.to_dict()]
    return jsonify(temp)
    
@app.route('/dev/api/v1/resources/get_address_by_id', methods=['GET'])
def retrieveAddressUsingId():
    address_id = request.args.get('id')
    address = easypost.Address.retrieve(address_id)
    
    return jsonify(address.to_dict())
    
@app.route('/dev/api/v1/resources/create_parcel', methods=['GET'])
def createParcel():
    weight = float(request.args.get('weight'))
    length = float(request.args.get('length'))
    height = float(request.args.get('height'))
    width = float(request.args.get('width'))
        
    parcel = easypost.Parcel.create(length = length, width = width, height = height, weight = weight)
    return jsonify(parcel.to_dict())
    
@app.route('/dev/api/v1/resources/get_parcel_by_id', methods=['GET'])
def retrieveParcelUsingId():
    parcel_id = request.args.get('id')
    parcel = easypost.Parcel.retrieve(parcel_id)
    
    return jsonify(parcel.to_dict())
    
@app.route('/dev/api/v1/resources/get_shipment_by_id', methods=['GET'])
def retrieveShipmentUsingId():
    shipment_id = request.args.get('id')
    shipment = easypost.Shipment.retrieve(shipment_id)
    
    return jsonify(shipment.to_dict())
    
@app.route('/dev/v1/resources/track_shipment', methods=['GET'])
def retrieveTrackingData():
    tracking_code = request.args.get('tracking_code')
    carrier = request.args.get('carrier')
    tracking_data = easypost.Tracker.create(tracking_code = tracking_code, carrier = carrier)
    
    temp = [tracking_data.to_dict()]
    return jsonify(temp)
    
app.run()
