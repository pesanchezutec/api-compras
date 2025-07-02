import boto3

def lambda_handler(event, context):
    # Entrada (json)
    compra = event['body']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.put_item(Item=compra)
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
