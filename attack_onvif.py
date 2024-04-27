import json

from onvif import ONVIFCamera

def onvif_live_video(target):
    with open("data/credentials.json", "r") as f:
        credentials = json.load(f)  
    ports = [6688, 8888, 80, 8080]

    for username in credentials["usernames"]:
        for password in credentials["passwords"]:
             for port in ports:
                try:
                    mycam = ONVIFCamera(target, port, username, password)  
                    media = mycam.create_media_service()
                    media_profile = media.GetProfiles()[0]
                    print(media_profile)
                    return
                except Exception as e: 
                    print(f"Onvif credentials : login : {username}/password : {password} - Failed on port {port}: {str(e)}")

