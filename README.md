# Simple Serverless-rest-api

Need to create 1 POST REST endpoint that will allow me to calculate time to load website. 
Request should allow to accept 1 or several websites
F.e. I sent https://google.com and https://facebook.com and API should return time in seconds to load them. 

AWS services to use AWS API Gateway, AWS Lambda. 

AWS credentials will be provided

It is ok to use frameworks like Serverless or AWS SAM.



## Solution on AWS
POST: https://8dooa9zguj.execute-api.us-east-1.amazonaws.com/Prod/

{"urls": ["https://google.com", "https://facebook.com"]}


