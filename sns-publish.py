#!/usr/bin/env python

import sys
from aws import SNS

topic = None
message = None
error_level = None

if (len(sys.argv) != 4):
    sys.exit(1) 
else:
    topic = sys.argv[1]
    message = sys.argv[2]
    error_level = sys.argv[3]

sns = SNS()
topic = sns.create_topic(topic)
topicARN = topic['TopicArn']
response = sns.publish_to_topic(topicARN, message + ":::" + error_level)
