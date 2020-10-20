import boto3

# Connect to DB; specify table.
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('memory_pill')

# Insert data example.
# table.put_item(Item={'Payload': {'Time': 'Tue Oct 19 12:32:37 2020'}, 'Time': 'Tue Oct 19 12:32:37 2020'})

# Delete data example.
# table.delete_item(Key={'Time': 'Tue Oct 19 12:32:37 2020'})

# Query all data.
response = table.scan()
items = response.get('Items', [])

# Loop through query results.
for item in items:
    print(item)
