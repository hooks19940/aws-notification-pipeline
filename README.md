# AWS Automated Notification Pipeline

An event driven cloud automation system built entirely on AWS.
Sends an automated email every day on a schedule no servers,
no manual work, just cloud services working together.

## How it works

EventBridge fires on a cron schedule → triggers a Lambda function
→ Lambda builds a message and publishes to SNS → SNS delivers
the email to my inbox automatically every day.

## AWS Services Used

- **EventBridge** — cron-based scheduler that triggers the pipeline
- **Lambda** — serverless function that builds and sends the message
- **SNS** — notification service that delivers the email
- **IAM** — permissions so Lambda can talk to SNS

## Architecture

EventBridge (scheduler) → Lambda (Python) → SNS → Email inbox

## What I learned

- How to build event-driven pipelines on AWS
- How serverless Lambda functions work
- How to use SNS for notifications
- How IAM permissions connect AWS services
- How cron scheduling works in the cloud
