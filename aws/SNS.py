import boto.sns

class SNS:
    def __init__(self):
        ''' SNS Instance '''
        self.region = 'eu-central-1'

    def create_topic(self, topic):
        ''' Create an return an SNS Topic '''
        conn = boto.sns.connect_to_region(self.region)

        topic = conn.create_topic(topic)
        
        return topic

    def publish_to_topic(self, target_arn, message):
        ''' Publish a message to an SNS Topic '''
        conn = boto.sns.connect_to_region(self.region)

        response = conn.publish(target_arn=target_arn, message=message)

        return response
