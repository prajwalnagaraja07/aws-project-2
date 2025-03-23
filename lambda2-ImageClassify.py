import json
import base64
import boto3
runtime = boto3.client('runtime.sagemaker')

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2025-03-23-08-28-30-019"

def lambda_handler(event, context):
    
    print('Input event:', event)

    # Decode the image data
    image = base64.b64decode(event['image_data'])
    
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image)
    
    inference = response['Body'].read().decode('utf-8')
    print('inference:', inference)
    
    # We return the data back to the Step Function    
    event["inferences"] = inference
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
    