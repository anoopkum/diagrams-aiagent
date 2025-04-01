import os
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.generic.database import SQL
from diagrams.aws.network import APIGateway
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from openai import AzureOpenAI
# Fallback for DynamoDB
try:
    from diagrams.aws.database import DynamoDB
except ImportError:
    from diagrams.generic.database import SQL as DynamoDB

# Azure OpenAI credentials
api_key = os.getenv("AZURE_API_KEY")
client = AzureOpenAI(
    azure_endpoint='https://ai-aihub01771178575364.services.ai.azure.com',
    api_key = os.getenv("AZURE_API_KEY"),
    api_version="turbo-2024-04-09"
)

def generate_architecture_description(prompt):
    """
    Use ChatGPT-4 to generate an architecture description.
    """

    system_message = {"role": "system", "content": "You are a helpful assistant that generates AWS architecture descriptions."}
    conversation = []
    conversation.append(system_message)    
    simulated_response = "S3, Cognito, API Gateway, Lambda, RDS, DynamoDB"
    return simulated_response

def create_diagram(description, output_file="aws_architecture"):
    """
    Create a diagram using the Diagrams library based on the description.
    """
    with Diagram(output_file, show=False, direction="LR"):
        # Define components
        user = S3("User")
        s3 = S3("S3 + CloudFront")
        cognito = Cognito("Cognito")
        api_gateway = APIGateway("API Gateway")
        lambda_function = Lambda("Lambda")
        rds = RDS("RDS")
        dynamodb = DynamoDB("DynamoDB")

        # Define connections based on the description
        if "S3" in description:
            user >> s3
        if "Cognito" in description:
            s3 >> cognito
        if "API Gateway" in description:
            cognito >> api_gateway
        if "Lambda" in description:
            api_gateway >> lambda_function
        if "RDS" in description:
            lambda_function >> rds
        if "DynamoDB" in description:
            lambda_function >> dynamodb

def main():
    # Step 1: Generate architecture description using ChatGPT-4
    prompt = "Generate an AWS architecture description for an e-commerce application."
    description = generate_architecture_description(prompt)
    print("Generated Description:\n", description)

    # Step 2: Create a diagram based on the description
    create_diagram(description, output_file="aws_ecommerce_architecture")
    print("Diagram created successfully!")
if __name__ == "__main__":
    main()