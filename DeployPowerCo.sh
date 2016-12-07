#!/bin/bash

# create the Lambda deployment package -- just a zip file
zip PowerCo-deployment.zip PowerCo.py

# publish the code to Lambda (the function must already exist)
aws --profile dixonaws@amazon.com --region us-east-1 lambda update-function-code --function-name PowerCo --zip-file fileb://PowerCo-deployment.zip --publish
