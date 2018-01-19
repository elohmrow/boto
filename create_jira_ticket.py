from jira import JIRA
import sys
import jira_creds

description = None

if (len(sys.argv) != 2):
    sys.exit(1)
else:
    description = sys.argv[1]

def ticket(description):
    options = { 'server': 'https://jira.magnolia-cms.com', }
    jira = JIRA(options, basic_auth=(jira_creds.login['username'], jira_creds.login['password']))

    issue_dict = {
        'project': 'SERVICES',
        'summary': 'Script ERROR',
        'description': description,
        'issuetype': 'Task',
    }

    new_issue = jira.create_issue(fields=issue_dict)
