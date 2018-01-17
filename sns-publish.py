#!/usr/bin/env python

import sys
from aws import SNS

topic = None
message = None

if (len(sys.argv) != 3):
    sys.exit(1) 
else:
    topic = sys.argv[1]
    message = sys.argv[2]

sns = SNS()
topic = sns.create_topic(topic)
topicARN = topic['CreateTopicResponse']['CreateTopicResult']['TopicArn']
response = sns.publish_to_topic(topicARN, message)
