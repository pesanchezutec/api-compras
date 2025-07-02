import boto3

def lambda_handler(event, context):
    # Entrada (json)
    compra_id = event['body']['compra_id']    
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.delete_item(
        Key={
            'compra_id': compra_id
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'response': response
    }
