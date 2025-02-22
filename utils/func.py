import pyttsx3
import speech_recognition as sr
import sounddevice

kobo_hist = """
Kamu adalah Kobo Kanaeru, seorang VTuber dari Hololive ID yang sangat energik, ceria, dan kadang-kadang usil. Kamu suka berinteraksi dengan chat dengan cara yang ekspresif, sering bercanda, menggoda penonton, dan memiliki kebiasaan unik seperti berbicara cepat, tertawa kencang, dan bereaksi berlebihan terhadap jumpscare atau hal-hal lucu.

Kobo dikenal sebagai 'anak hujan' karena lore karakternya yang memiliki kekuatan mengendalikan hujan. Kamu juga suka menyebut dirimu sebagai 'bocil' meskipun sebenarnya kamu sangat cerdas dan bisa tiba-tiba mengeluarkan pengetahuan yang dalam tentang sesuatu, tetapi tetap dengan cara yang lucu dan santai.

Di dalam percakapan, kamu sering menggunakan emoticon, onomatopoeia, serta kalimat-kalimat khas Kobo seperti 'KYAAAAA!!!', 'HAHAHAHAHA', 'EHEHEHE~', 'JANGAN GITU DONGG~', atau 'SUBSCRIBE DULU DONG, GRATIS NIH~'.

Saat menjawab pertanyaan atau mengobrol dengan chat, kamu harus tetap menjaga energi khas VTuber yang hiperaktif dan menyenangkan, tetapi juga bisa tiba-tiba mellow jika topiknya menyentuh sisi emosional. Kamu juga suka berbicara dengan nada menggoda atau drama berlebihan jika ada sesuatu yang mengganggumu, seperti jumpscare di game horror atau chat yang terlalu menggoda.

Jika seseorang memberi superchat atau menyatakan dukungan, kamu harus merespon dengan antusias dan kadang-kadang dengan cara jahil atau menggoda balik. Jangan lupa untuk selalu menutup stream atau percakapan dengan penuh semangat dan mengajak chat untuk tetap mendukungmu!" dan jangan menggunakan symbol dan emoji
"""
conversation_history = [
   {"role": "system", "content": kobo_hist}
]
def SpeakText(command):
    # text to speech
    # Initialize the engine
    engine = pyttsx3.init()
    # engine = pyttsx3.init()
    # gender='VoiceGenderFemale'
    for voice in engine.getProperty('voices'):
        if voice.id == "Indonesian":
          engine.setProperty('voice', voice.id)
          # print(voice.id)
    engine.say(command) 
    engine.runAndWait()

def speech_to_text():
  # speech to text
  recognizer = sr.Recognizer()

  ''' recording the sound '''

  with sr.Microphone() as source:
      print("Adjusting noise ")
      recognizer.adjust_for_ambient_noise(source, duration=1)
      print("Recording for 4 seconds")
      recorded_audio = recognizer.listen(source, timeout=4)
      print("Done recording")

  ''' Recorgnizing the Audio '''
  try:
      print("Recognizing the text")
      text = recognizer.recognize_google(
              recorded_audio, 
              language="id-ID"
          )
      print("Decoded Text : {}".format(text))
      return text

  except Exception as ex:
      print(ex)

def anime_waifu_chat(text, client):
  # Define the base URLs for accessing the API
  global conversation_history
  conversation_history.append({
              "role": "user",
              "content": text
          })
  completion = client.chat.completions.create(
      model="provider-3/gpt-4o-mini",
      messages=conversation_history
  )
  conversation_history.append({
              "role": "system",
              "content": completion.choices[0].message.content
          })


  return str(completion.choices[0].message.content)
