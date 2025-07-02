import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    compra_id = body.get('compra_id')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.delete_item(
        Key={ 'compra_id': compra_id }
    )

    return {
        'statusCode': 200,
        'response': response
    }
