# Sick-Leaf---Treatment-

此次project是分辨植物是否生病
1. 如果生病的話，樹莓派會說出治療方法給使用者
2. 如果判斷為健康會顯示健康，使用者不用擔心。
<br/>
<br/>

使用技術
1. opencv 顯示植物健康情況
2. tensorflow (train data)
3. 語音azure speech 服務
<img width="1435" alt="螢幕截圖 2022-06-06 下午6 28 57" src="https://user-images.githubusercontent.com/85872659/172144098-9f13eac6-ff2e-49e2-8a9e-aa7fc3c35906.png">


告訴使用者他們植物是健康
```
    cv2.putText(image, "Health", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
```

告訴使用者他們植物感染真菌，使用opencv2
<img width="956" alt="螢幕截圖 2022-06-06 下午8 35 13" src="https://user-images.githubusercontent.com/85872659/172161956-09dddbd5-b7c1-4236-b0a0-a9e161ba5ba3.png">
```
cv2.putText(image, "Downy Mildew", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
```


說出治療方法
```
text = 
'Plant resistant cultivars when available No fungicides are available, 
but cultural practices can help. Remove and destroy infected foliage, 
or entire plants if downy mildew is prevalent. Avoid crowding plants 
or watering them in the evening, and rotate edibles year to year'

speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
```

更進一步開發
1. 增加病種類和病徵 (暫時只有一種病-真菌)
2. 增加train data 暫時還是不太精確
3. 樹莓派 好卡，如果同時使用語音 和 影像。
