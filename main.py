import sounddevice
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import os
from utils.func import anime_waifu_chat, speech_to_text
from utils.text_to_voice import generate_voice, translate_to_japanese
import playsound

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")


from openai import OpenAI

BASE_URLS = [
    'https://api-handler-ddc-free-api.hf.space/v2',
    'https://devsdocode-ddc-free-api.hf.space/v2',
    'https://free-ddc.xiolabs.xyz/v1',
    'https://api.ddc.xiolabs.xyz/v1'
]

STATUS = "https://test-company-2.betteruptime.com/"

client = OpenAI(
  base_url=BASE_URLS[-1],  # Using the third URL in the list
  api_key="Free-For-YT-Subscribers-@DevsDoCode-WatchFullVideo",
)
# print(client.models.list())

# speaker_id = int(input("Masukkan ID speaker (contoh: 1 untuk suara default): "))
while True:
  user_text = input("Masukkan teks yang ingin diubah menjadi suara: ")
  # user_text = speech_to_text()
  # translated_text = translate_to_japanese(user_text)
  waifu = anime_waifu_chat(text=user_text, client=client)
  from gradio_client import Client, handle_file

  clientG = Client("http://127.0.0.1:7860/")
  print(waifu)
  result = clientG.predict(
      name="Kobo Kanaeru",
      path="weights/hololive-id/Kobo/kobohololiveid.pth",
      index="weights/hololive-id/Kobo/added_IVF3009_Flat_nprobe_1_kobohololiveid_v2.index",
      vc_input="Hello!!",
      vc_upload=handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),
      tts_text=waifu,
      tts_voice="Indonesian-Ardi- (Male)",
      # tts_voice="English-Ana (Female)",Javanese (Indonesia)-Dimas- (Male)
      f0_up_key=12,
      f0_method="rmvpe",
      index_rate=0.4,
      filter_radius=1,
      resample_sr=0,
      rms_mix_rate=1,
      protect=0.5,
      api_name="/infer"
  )
  playsound.playsound(result[1])


  # translated_waifu = translate_to_japanese(waifu)
  # print("Aini ID : ", waifu)
  # print("Aini JAPAN : ", translated_waifu)
  # generate_voice(translated_waifu, speaker=speaker_id)


