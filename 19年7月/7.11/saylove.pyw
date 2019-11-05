import win32com.client

spk = win32com.client.Dispatch("SAPI.SpVoice")

spk.Speak("安红，我爱你")

# 改成pyw 可以不出现黑屏界面