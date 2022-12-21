# Import the OneNote API
import onenote_api

# Get the user's OneDrive for Business client
client = onenote_api.OnenoteClient()

# Sign the user out of OneNote
client.sign_out()

# Sign the user back in to OneNote
client.sign_in()

# Sync the user's notes
client.sync()
