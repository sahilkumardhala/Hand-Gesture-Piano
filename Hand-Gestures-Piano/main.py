
import cv2 # pip install openCV
from cvzone.HandTrackingModule import HandDetector # pip install cvZone
import pyglet # pip install pyglet
import threading # pip install threading

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

window = pyglet.window.Window()
detector = HandDetector(detectionCon=0.8)

# List of the piano keys.
keys = [["C", "D", "E", "F", "G", "A", "B", "C", "D", "E", "F", "G", "A", "B"],
        ["C#", "D#", "F#", "G#", "A#", "C#", "D#", "F#", "G#", "A#"]]

class Button():
    def __init__(self, pos, text, size, color):
        self.pos = pos
        self.size = size
        self.text = text
        self.color = color

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if i == 0:
            buttonList.append(Button([38 * j + 15, 80], key, [35, 100], (225, 255, 255)))
        else:
            buttonList.append(Button([(40 + j) * j + 25, 80], key, [35, 50], (0, 0, 0)))

def play_sound(sound):
    sound.play()


def playkeys(button):
    if button.text=="A":
            
        effectA=pyglet.resource.media("A.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectA,)).start()
                  
    elif button.text=="B":
            
        effectB=pyglet.resource.media("B.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectB,)).start()
                
    elif button.text=="C":
            
        effectC=pyglet.resource.media("C.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectC,)).start()

    elif button.text=="D":
            
        effectD=pyglet.resource.media("D.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectD,)).start()

    elif button.text=="E":
            
        effectE=pyglet.resource.media("E.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectE,)).start()
        

    elif button.text=="F":
            
        effectF=pyglet.resource.media("F.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectF,)).start()

    elif button.text=="G":
            
        effectG=pyglet.resource.media("G.wav",streaming=False)
        threading.Thread(target=play_sound, args=(effectG,)).start()

    else:
        print("Playing sound for", button.text)

def display_video():
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        hands, img = detector.findHands(img)

        # Draw buttons and check for hand over buttons
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            colorr = button.color
            cv2.rectangle(img, (x, y), (x + w, y + h), colorr, cv2.FILLED)
            cv2.putText(img, button.text, (x + 10, y + h - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (214, 0, 220), 2)

            if hands and x < hands[0]['lmList'][8][0] < x + w and y < hands[0]['lmList'][8][1] < y + h:
                playkeys(button)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Start the video display in a separate thread
video_thread = threading.Thread(target=display_video)
video_thread.start()

# Wait for the video thread to finish
video_thread.join()

# Release the video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
