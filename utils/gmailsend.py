#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: gmailsend.py

# This script will open a new window in your default web browser and ask you to authorize the script to send emails on your behalf. Once you've authorized it, the script will store your access and refresh tokens in a file named `token.pickle`, so you won't have to re-authorize it every time you run the script.

# Please note that you'll need to create a project in the Google Cloud Console, enable the Gmail API, and download the OAuth2 credentials file in order to use this script. You can find instructions on how to do this in the [Python Quickstart guide for the Gmail API](https://developers.google.com/gmail/api/quickstart/python).


from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os.path
import base64
import os
import pickle
from pyperclip import paste


#  Here is a script that uses OAuth2 for authentication. This script uses the `google-auth`, `google-auth-oauthlib`, `google-auth-httplib2`, and `google-api-python-client` libraries, which you can install with pip.
# Replace `credentials.json` with the path to your OAuth2 credentials file.

class ClipnPaste:
    """
    This one just grabs system clipart memory and return it
    """

    def __init__(self):
        self.data = paste()

    def __str__(self):
        data = self.data.strip()
        return data


# If you modify these SCOPES, you have to delete the file token.pickle.
# the token.pickle file stores the user's access and refresh tokens.
# That way you dont need to authenticate every time you run the script.
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
]


def main():
    creds = None
    # Check if we have valid credentials
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If we don't have valid credentials, we need to get some
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
            flow = InstalledAppFlow.from_client_secrets_file(
                "$HOME/.config/gcloud/client_secret_gmailsend.apps.googleusercontent.com.json",
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)


    # Build the service
    service = build("gmail", "v1", credentials=creds)

    # Check user's profile
    profile_info = service.users().getProfile(userId="me").execute()
    print(f"Current user's email: {profile_info['emailAddress']}")

    # The copied data will be used as the email body
    email_body_data = ClipnPaste()

    # Userinputs
    mailto = input("Recipient's email address: ")
    subject = input("Email subject: ")
    body = str(email_body_data)  # input("Email body: ")
    file_path = input("Path to the attachment (leave blank if no attachment): ")

    msg = MIMEMultipart()
    msg["To"] = mailto
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))
    if file_path:  # If file_path is not empty
        with open(file_path, "rb") as file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                'attachment; filename="{}"'.format(os.path.basename(file_path)),
            )
            msg.attach(part)

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    raw_msg = {"raw": raw}
    message = service.users().messages().send(userId="me", body=raw_msg).execute()


if __name__ == "__main__":
    main()
