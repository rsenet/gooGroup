from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/admin.directory.user', 'https://www.googleapis.com/auth/admin.directory.group', 'https://www.googleapis.com/auth/apps.groups.settings']
SERVICE_ACCOUNT_FILE = 'credz.json'

# Authentication
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject="EMAIL OF YOUR ADMIN ACCOUNT")

# Retrieve all groups
service = build('admin', 'directory_v1', credentials=credentials)
response_group = service.groups().list(customer='my_customer').execute()

# Retrieve group settings
service = build("groupssettings", "v1", credentials=credentials)

# Display group settings
for group in response_group['groups']:
    group_info = service.groups().get(groupUniqueId=group['email']).execute()

    print(group['email'])
    print("-" * len(group['email']))
    print("Who Can Join: " + group_info["whoCanJoin"])
    print("Who Can View Member: " + group_info["whoCanViewMembership"])
    print("Who Can View Group: " + group_info["whoCanViewGroup"])
    print("Who Can Invite : " + group_info["whoCanInvite"])
    print("Who Can Add : " + group_info["whoCanAdd"])
    print("Who Can Post Message : " + group_info["whoCanPostMessage"])
    print("External members allowed: " + group_info["allowExternalMembers"])
    print()