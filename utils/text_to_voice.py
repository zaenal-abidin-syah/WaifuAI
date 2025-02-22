import requests
# from googletrans import Translator
from playsound import playsound
# from google_trans_new import google_translator
from deep_translator import GoogleTranslator
def translate_to_japanese(text):
    """
    Menerjemahkan teks ke bahasa Jepang menggunakan Google Translate.

    Args:
        text (str): Teks yang akan diterjemahkan.

    Returns:
        str: Teks yang telah diterjemahkan ke bahasa Jepang.
    """
    try:
        # translator = Translator()
        # translated = translator.translate(text, src="id", dest="ja")
        # return translated.text
        return GoogleTranslator(source='id', target='ja').translate(text)
    except Exception as e:
        print(f"Terjadi kesalahan saat menerjemahkan: {e}")
        return text  # Jika terjadi kesalahan, gunakan teks asli.

# def translate_to_japanese(text):
#     """
#     Menerjemahkan teks ke bahasa Jepang menggunakan google_trans_new.

#     Args:
#         text (str): Teks yang akan diterjemahkan.

#     Returns:
#         str: Teks yang telah diterjemahkan ke bahasa Jepang.
#     """
#     try:
#         translator = google_translator()
#         translated = translator.translate(text, lang_tgt='ja')
#         return translated
#     except Exception as e:
#         print(f"Terjadi kesalahan saat menerjemahkan: {e}")
#         return text  # Jika terjadi kesalahan, gunakan teks asli.

def generate_voice(text, speaker=1, output_file="output.wav"):
    """
    Menggunakan Voicevox untuk menghasilkan suara dari teks.

    Args:
        text (str): Teks yang akan dikonversi menjadi suara.
        speaker (int): ID speaker untuk menentukan jenis suara. Default: 1.
        output_file (str): Nama file output untuk audio. Default: "output.wav".
    """
    try:
        # Langkah 1: Generate query
        query_payload = {"text": text, "speaker": speaker}
        query_url = "http://localhost:50021/audio_query"
        query_response = requests.post(query_url, params=query_payload)
        if query_response.status_code != 200:
            print(f"Error in audio_query: {query_response.text}")
            return

        # Langkah 2: Synthesize voice
        synthesis_url = "http://localhost:50021/synthesis"
        synthesis_response = requests.post(
            synthesis_url,
            params={"speaker": speaker},
            data=query_response.content
        )
        if synthesis_response.status_code != 200:
            print(f"Error in synthesis: {synthesis_response.text}")
            return

        # Menyimpan audio ke file
        with open(output_file, "wb") as audio_file:
            audio_file.write(synthesis_response.content)
        print(f"Audio berhasil disimpan sebagai {output_file}")
        playsound(output_file)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# if __name__ == "__main__":
#     print("Selamat datang di Voicevox TTS!")
#     user_text = input("Masukkan teks yang ingin diubah menjadi suara: ")
#     translated_text = translate_to_japanese(user_text)
#     speaker_id = int(input("Masukkan ID speaker (contoh: 1 untuk suara default): "))
#     generate_voice(translated_text, speaker=speaker_id)
