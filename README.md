# Rapid-Scheduler

A scheduling platform application utilizing Python and AWS, implementing serverless architecture through Lambda and DynamoDB.

# Step 1: Environment and AWS Setup
Before you start, make sure you have:

AWS Account: Configure your AWS account.

AWS CLI: Installed and configured on your machine with appropriate permissions.

Python: Ensure Python (version 3.8 or higher) is installed.

Virtualenv: Recommended for creating an isolated Python environment.

AWS SDKs: Boto3 for DynamoDB interactions.

# Step 2: Install Required Packages through bash
Create a virtual environment and install necessary packages:

python -m venv venv

source venv/bin/activate

pip install flask aws-sam-cli boto3

pip install aws-wsgi

You can then clone/download the codebase to the local project folder.

# Step 3: Running the Application 
Build and Deploy your application by navigating to your project directory and run the following command to build your application:

sam build

This command packages your application and its dependencies into a deployment-ready format.

To deploy your application, run the following:

sam deploy --guided

The --guided flag provides a step-by-step interactive deployment process, where you can specify settings such as the stack name, AWS region, and other configuration details related to your AWS account.

After deployment, AWS CloudFormation outputs the API Gateway URL, where you can access the Flask application via the URL.
