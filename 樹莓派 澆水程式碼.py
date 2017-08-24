import RPi.GPIO
import time
RPi.GPIO.setmode(RP.GPIO.BCM) #以BCM模式選電路
RPi.GPIO.setup(14,RPi.GPIO.OUT)
while True:
	try:
		if time.strftime("%H") == '7':
			try:
				RPi.GPIO.output(14,True)() #記得對到電路，如果不是BCM街口則是8
				time.sleep(10) #澆水十秒
				RPi.GPIO.output(14,False)

			except:
				print("時間出現錯誤")
		time.sleep(3600) #休息一小時，直到不再是七點
		RPi.GPIO.cleanup #好習慣
	except:
		print("主程式出現問題")