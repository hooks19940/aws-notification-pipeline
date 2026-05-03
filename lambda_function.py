import boto3
from datetime import datetime

def lambda_handler(event, context):

    SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

    today = datetime.now().strftime("%A, %B %d, %Y")

    subject = f"Your Daily Cloud Notification — {today}"

    message = f"""
Hello!

This is your automated daily notification from AWS.

Date: {today}

This message was sent automatically by:
- AWS EventBridge (scheduled the trigger)
- AWS Lambda (ran this code)
- AWS SNS (delivered this email)

No servers. No manual work. Just cloud automation.

— Your AWS Notification System
    """

    sns = boto3.client('sns', region_name='us-east-2')

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject,
        Message=message
    )

    return {
        'statusCode': 200,
        'body': 'Notification sent successfully!'
    }
