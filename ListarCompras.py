import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('compras')
    response = table.scan()  # Lee todos los registros
    items = response.get('Items', [])
    num_reg = response.get('Count', 0)

    return {
        'statusCode': 200,
        'num_reg': num_reg,
        'compras': items
    }
