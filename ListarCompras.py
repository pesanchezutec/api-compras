import boto3

def lambda_handler(event, context):
    # Entrada (json)
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.scan() # Lee todos los registros
    items = response['Items']
    num_reg = response['Count']
    # Salida (json)
    return {
        'statusCode': 200,
        'num_reg': num_reg,
        'compras': items
    }
