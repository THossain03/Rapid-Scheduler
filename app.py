from flask import Flask, request, jsonify
import boto3
from boto3.dynamodb.conditions import Key
import os
from datetime import datetime

app = Flask(__name__)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')  # Modify as per your region
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE', 'Events'))

@app.route('/')
def get_events():
    # Get the current date and query DynamoDB for events on this date
    today = datetime.now().strftime('%Y-%m-%d')
    response = table.query(
        KeyConditionExpression=Key('date').eq(today)
    )
    events = response.get('Items', [])
    return jsonify(events)

@app.route('/event', methods=['POST'])
def add_event():
    event = request.get_json()
    event['timestamp'] = datetime.now().isoformat()
    table.put_item(Item=event)
    return jsonify({'message': 'Event added successfully!'}), 201

@app.route('/event/<event_id>', methods=['PUT'])
def update_event(event_id):
    updates = request.get_json()
    updates['event_id'] = event_id  # Ensure the event ID is part of the update payload
    expression = "set "
    expression_attr_values = {}
    for key, val in updates.items():
        expression += f"{key} = :{key},"
        expression_attr_values[f":{key}"] = val
    expression = expression.rstrip(',')

    response = table.update_item(
        Key={'event_id': event_id},
        UpdateExpression=expression,
        ExpressionAttributeValues=expression_attr_values,
        ReturnValues='UPDATED_NEW'
    )
    return jsonify(response['Attributes']), 200

@app.route('/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    table.delete_item(Key={'event_id': event_id})
    return jsonify({'message': 'Event deleted successfully!'}), 204

# Lambda handler using AWS WSGI
from aws_wsgi import make_lambda_handler
lambda_handler = make_lambda_handler(app)
