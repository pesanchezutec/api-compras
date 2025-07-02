import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    compra_id = event['body']['compra_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.query(
        KeyConditionExpression=Key('compra_id').eq(compra_id)
    )
    items = response['Items']
    # Salida (json)
    return {
        'statusCode': 200,
        'response': items
    }
