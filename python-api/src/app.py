import json
import boto3
import uuid
import bcrypt

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('usersDB')

def fetch_all_users(event, context):
    response = table.scan()
    users = response.get('Items', [])
    return {
        "statusCode": 200,
        "body": json.dumps({"users": users})
    }

def create_user(event, context):
    body = json.loads(event['body'])
    response = table.scan(
        FilterExpression="username = :u OR email = :e",
        ExpressionAttributeValues={
            ":u": body['username'],
            ":e": body['email']
        }
    )
    if response['Items']:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Username or email already exists"})
        }
    hashed_password = bcrypt.hashpw(body['password'].encode('utf-8'), bcrypt.gensalt())
    user = {
        'id': str(uuid.uuid4()),
        'username': body['username'],
        'email': body['email'],
        'password': hashed_password.decode('utf-8')  # String DynamoDB
    }
    table.put_item(Item=user)
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User created successfully"})
    }

def delete_user(event, context):
    user_id = event['pathParameters']['id']
    table.delete_item(Key={'id': user_id})
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User deleted successfully"})
    }

def update_user(event, context):
    user_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    
    hashed_password = bcrypt.hashpw(body['password'].encode('utf-8'), bcrypt.gensalt())
    table.update_item(
        Key={'id': user_id},
        UpdateExpression="set username=:u, email=:e, password=:p",
        ExpressionAttributeValues={
            ':u': body['username'],
            ':e': body['email'],
            ':p': hashed_password.decode('utf-8')
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User updated successfully"})
    }
    