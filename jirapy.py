from jira import JIRA
import secrets

jira_options = {'server': secrets.serverName}
jira = JIRA(options=jira_options,
            basic_auth=(secrets.userName,
                        secrets.password))

issue = jira.issue('SVDSK-19566')
# for  comment in issue.fields.comment.comments:
#     print comment.author.displayName
#     print comment.body
summary = issue.fields.summary
description = issue.fields.description
type = issue.fields.issuetype.name
priority = issue.fields.priority.name
status = issue.fields.status.name
assignee = issue.fields.assignee.name
reporter = issue.fields.reporter.name
commentList = []
for comment in issue.fields.comment.comments:
    comments = {
        'name': comment.author.name,
        'body': comment.body
    }
    commentList.append(comments)
print commentList
