import numpy as np
import cv2
from time import sleep
import json
import tensorflow as tf
from PIL import Image
import pyautogui
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="", region="eastus")
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Get text from the console and synthesize to the default speaker.
print("Enter some text that you want to speak >")
text = 'Plant resistant cultivars when available No fungicides are available, but cultural practices can help. Remove and destroy infected foliage, or entire plants if downy mildew is prevalent. Avoid crowding plants or watering them in the evening, and rotate edibles year to year'
current_x = 300
move = 10
width, _ = pyautogui.size()

with open("signature.json", "r") as f:
    signature = json.load(f)
inputs = signature.get('inputs')
labels = signature.get('classes')['Label']
#print(labels)

model = tf.saved_model.load('.')
input_width, input_height = inputs["Image"]["shape"][1:3]

cap = cv2.VideoCapture(0)
while True:
    success, image = cap.read()
    if success == True:
        image = cv2.flip(image,1) #左右反轉
        img = Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
        img = img.resize((input_width, input_height))
        img = np.asarray(img, dtype=np.float32) / 255.0
        img = np.expand_dims(img, axis=0)
        
        predict = model.signatures["serving_default"](tf.constant(img))['Confidences'][0]
        index = np.argmax(predict, axis=-1)
        classname = labels[index]
        print(current_x, classname)
		
        if classname == 'health':
            cv2.putText(image, "Health", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            current_x -= move
            if current_x < 0:
                current_x = 0
        elif classname == 'sick':
            cv2.putText(image, "Downy Mildew", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
            current_x += move
            if current_x > width:
                current_x = width
        elif classname == 'normal':
            print('normal')
        cv2.imshow("Frame",image)
        sleep(0.2)
		           	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()	