import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # event['body'] debe tener { "compra_id": "COMP-0001" }
    import json
    body = json.loads(event.get('body', '{}'))
    compra_id = body.get('compra_id')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.query(
        KeyConditionExpression=Key('compra_id').eq(compra_id)
    )
    items = response.get('Items', [])

    return {
        'statusCode': 200,
        'response': items
    }
