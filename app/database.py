import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="sa-east-1"
)

def get_table():
    return dynamodb.Table("clima_dados")