# Import the Microsoft Graph API client
import graph_api_client

# Get the user's OneDrive client
client = graph_api_client.OneDriveClient()

# Sync the user's OneDrive folders
client.sync()

# Sign the user out of OneDrive
client.sign_out()

# Sign the user back in to OneDrive
client.sign_in()

# Import the OneNote API
import onenote_api

# Get the user's OneDrive for Business client
client = onenote_api.OnenoteClient()

# Sync the user's OneNote notes
client.sync()

# Sign the user out of OneNote
client.sign_out()

# Sign the user back in to OneNote
client.sign_in()
