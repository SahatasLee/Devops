import requests

# Replace 'YOUR_ACCESS_TOKEN' with the access token you obtained from Line Notify.
access_token = 'b1k7RshlkYsKdjOUtMCLGhx4HiGLFbZB2LbNsajdCc5'

# Define the message you want to send.
message = 'Hello, Line Notify!'

# Line Notify API endpoint
url = 'https://notify-api.line.me/api/notify'

# Set the headers with the access token.
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Set the message payload.
data = {
    'message': message
}

# Send the message using POST request.
response = requests.post(url, headers=headers, data=data)

# Check the response status.
if response.status_code == 200:
    print('Message sent successfully!')
else:
    print(f'Failed to send message. Status code: {response.status_code}')
    print(response.text)