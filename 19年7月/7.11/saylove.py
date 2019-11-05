import win32com.client

spk = win32com.client.Dispatch("SAPI.SpVoice")

spk.Speak("安红，我爱你")

# 逗死我了
# CreateObject("SAPI.SpVoice").
# Speak "wo me you wen hua, wo zhi hui zhong tian"