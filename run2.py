from twilio.rest import Client
from dotenv import load_dotenv
import os
import json

# Your Account SID and Auth Token from twilio.com/console
load_dotenv()  # take environment variables from .env.
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
workspace_sid = os.getenv('WORKSPACE_SID')
client = Client(account_sid, auth_token)


def run():
    conversations = [] # List of all active conversations
    # Fetch all active conversations

    for conversation in client.conversations.v1.conversations.list():
        if(conversation.state == 'active'):
            conversations.append(conversation)

    task_conversation_sids = [] # Get list of tasks with conversation SIDs
    # Create a set of conversation SIDs that have associated tasks
    for task in client.taskrouter.v1.workspaces(workspace_sid).tasks.list():
        json_obj = json.loads(task.attributes)
        if 'conversationSid' in json_obj:
            task_conversation_sids.append(json_obj["conversationSid"])

    # Filter conversations that don't have associated tasks
    if len(conversations) > 0:
        conversations_without_tasks = [conversation for conversation in conversations if conversation.sid not in task_conversation_sids]

        for conversation in conversations_without_tasks:
            print(f"Conversations without task: {conversation.sid}")
    else:
        print("No active conversations found")
        return



if __name__ == "__main__":
    run() 