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

    # Tutorial provided from in the project description does not work. 
    # So instead I used method suggested in the forum: https://knowledge.udacity.com/questions/767689, which does not need any other installation procedures.
    
    # # Instantiate a Predictor
    # predictor = sagemaker.predictor.Predictor(
    #     ENDPOINT,
    #     sagemaker_session=sagemaker.Session()
    # )

    # # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")
    
    # # Make a prediction:
    # inferences = predictor.predict(image)
    
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
    

# Test vector:
# {
#     "image_data": "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",
#     "s3_bucket": "sagemaker-us-east-1-071394031625",
#     "s3_key": "test/bicycle_s_000513.png"
# }