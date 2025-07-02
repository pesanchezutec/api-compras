import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    compra = body

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.put_item(Item=compra)

    return {
        'statusCode': 200,
        'response': response
    }
