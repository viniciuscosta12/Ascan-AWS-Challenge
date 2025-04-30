# Ascan-AWS-Challenge

## Sumary

- [AWS Ascan](#aws-ascan)
    - [About the project](#about-the-project)
        - [API Features](#api-features)
    - [Technologies](#technologies)
    - [Project Structure](#project-structure)
    - [Getting Started](#getting-started)
        - [Prerequisites](#prerequisites)
        - [Build and Deploy](#build-and-deploy)
        - [Local Test](#local-test)
        - [Cleanup](#cleanup)


## AWS Ascan

This project is part of the conclusion of a AWS beggining training program at [Instituto Altântico](https://www.atlantico.com.br/). The primary goal was to develop a serverless REST API, using AWS Lambda, DynamoDB, and defined with infrastructure as code via AWS SAM (Serverless Application Model).

## About the project

This project is a simple REST API built with Python to perform basic user management operations such as creating, updating, retrieving, and deleting users. The application is designed to run on AWS Lambda, leveraging serverless architecture for scalability and cost efficiency. The data is stored in a DynamoDB table configured for on-demand billing (PAY_PER_REQUEST).
All infrastructure components — including the Lambda functions, API Gateway routes, and DynamoDB table — are provisioned using AWS SAM (Serverless Application Model), embracing the Infrastructure as Code (IaC) approach. This ensures consistency and easy redeployment across environments.
For demonstration purposes, authentication was not enforced, but the architecture supports the addition of a Lambda Authorizer for token-based access control. The API can be tested locally using SAM CLI or deployed to AWS for public access.

### API Features

- Create user  (`POST /CreateUser`)
- Fetch all users (`GET /FetchAllUsers`)
- Update user (`PUT /UpdateUser/{id}`)
- Delete user (`DELETE /DeleteUser/{id}`)

## Technologies

- Python 3.11
- AWS Lambda
- Amazon DynamoDB
- AWS SAM
- CloudFormation (IaC)

## Project Structure

```
.
├── python-api/
│   └── src/
│       ├── app.py           # Main API code
│       └── requirements.txt # Python dependencies
├── template.yaml            # Infrastructure as code (AWS SAM)
└── README.md                # This file
```

## Getting Started

### Prerequisites

- AWS account with necessary permissions to create Lambda functions, DynamoDB tables, and API Gateway endpoints.
- AWS CLI installed and configured with your AWS credentials.
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) installed.
- Python 3.11 installed on your local machine.
- Docker installed and running (equired for `sam build`).
- An existing S3 bucket in your AWS account for storing deployment artifacts.
>Tip: You can create one using the AWS CLI:
aws s3 mb s3://your-bucket-name --region $AWS_REGION

### Build and Deploy

1. **Install dependencies**:
   ```bash
   pip install -r python-api/src/requirements.txt
   ```

2. **Build**:
   ```bash
   sam build
   ```

3. **Deploy**:
   ```bash
   sam deploy --guided
   ```

   Siga as instruções e escolha um nome para a stack. Exemplo: `ascan-api-stack`.

### Local Test

You can test an API locally with the SAM CLI:
```bash
sam local start-api
```

Then use Postman or cURL to interact with the endpoints.

### Cleanup

To remove all resources created by this project:
```bash
sam delete
```
This command deletes the deployed stack, including all associated AWS resources (e.g., Lambda functions, API Gateway, DynamoDB tables, etc.).
Make sure you are in the project directory where the `template.yaml` is located and that your AWS credentials are properly configured.