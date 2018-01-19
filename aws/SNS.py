import boto3

class SNS:
    def __init__(self):
        ''' SNS Instance '''
        self.region = 'eu-central-1'

    def create_topic(self, topic):
        ''' Create an return an SNS Topic '''
        client = boto3.client(
            'sns',
            region_name=self.region
        )
        topic = client.create_topic(Name=topic)
        
        return topic

    def publish_to_topic(self, topicARN, message):
        ''' Publish a message to an SNS Topic '''
        client = boto3.client(
            'sns',
            region_name=self.region
        )

        response = client.publish(TopicArn=topicARN, Message=message)

        return response
