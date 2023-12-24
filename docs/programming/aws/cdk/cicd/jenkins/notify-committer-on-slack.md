Notify committer on slack
===

Jenkins helper function
---

```groovy
def createSlackMessage(String baseMessage, Map newDetails = [:], String additional = null) {

    def commonDetails = [
            "_commit_": "<${env.GIT_COMMIT_URL}|${env.GIT_MESSAGE_TRIMMED}>",
            '_author_': env.SLACK_USER_DETAILS
        ]
    def details = commonDetails.clone()
    details.putAll(newDetails)

    def message = "${baseMessage}\n"
    
    details.each { key, value ->
        message += "${key}: ${value}\n"
    }

    message += "<${env.RUN_DISPLAY_URL}|deployment>"

    if (additional) {
        message += "\n${additional}"
    }
    
    return message
}
```

Jenkinsfile stage
---

```groovy
    stage('Some stage') {
      agent {
        docker {
          image 'company/image:13'
        }
      }
      steps {
          script {
              env.GIT_MESSAGE_TRIMMED = sh(returnStdout: true, script: 'echo "$(git --no-pager log --oneline --format=%B -n 1 $GIT_COMMIT | head -n 1)"').trim()
              env.GIT_AUTHOR_NAME = sh(returnStdout: true, script: 'echo "$(git --no-pager log -1 --pretty=format:%an)"').trim()
              env.GIT_COMMIT_URL = sh(returnStdout: true, script: 'echo "https:///<link_to_repo>/commit/$GIT_COMMIT"').trim()
              env.SLACK_USER_DETAILS = sh(returnStdout: true, script: 'python3 get_slack_details.py "$GIT_AUTHOR_NAME"').trim()
          }
        sh 'printenv'
        script {
            if (env.BRANCH_NAME == 'master') {
                slackSend(channel: '#channel', color: '#ffff00', message: createSlackMessage("🔔 Starting to deploy change", [ '_env_': '`qa`' ], "Wait till this deployment goes through before merging any PR."))
            }
        }
        sh 'build'
        sh 'commands'
        sh 'go'
        sh 'here'
      }
      post {
        failure {
            slackSend(channel: '#channel', color: 'danger', message: createSlackMessage("❌ Deployment failed.", [ '_env_': '`qa`' ]))
        }
      }
    }
```

Helper file
---

```python
import sys

SKIPPED_NAMES = ["<some_name>"]

MAPPER = {
    "<git name>": "@<slack_user_id>",
}


def print_slack_details(name: str):
    if len(name) == 0:
        return
    if name in SKIPPED_NAMES:
        return

    if name in MAPPER.keys():
        slack_mention = MAPPER[name]
        print(f"<{slack_mention}>")
    else:
        print(name)


if __name__ == "__main__":
    name = sys.argv[1]
    print_slack_details(name)
```
