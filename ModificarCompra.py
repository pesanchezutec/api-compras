import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    compra_id = body.get('compra_id')
    datos = body.get('datos', {})

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.update_item(
        Key={ 'compra_id': compra_id },
        UpdateExpression="SET datos = :d",
        ExpressionAttributeValues={ ':d': datos },
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'response': response
    }
