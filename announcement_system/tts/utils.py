# tts/utils.py

import os
from django.conf import settings
from transformers import VitsModel, AutoTokenizer
import torch
import scipy
import re
from num2words import num2words
from pydub import AudioSegment
import logging

def kyrgyz_num2words(num):
    # Kyrgyz number words
    ones = ['', 'бир', 'эки', 'үч', 'төрт', 'беш', 'алты', 'жети', 'сегиз', 'тогуз']
    tens = ['', 'он', 'жыйырма', 'отуз', 'кырк', 'элүү', 'алтымыш', 'жетимиш', 'сексен', 'токсон']
    scales = ['', 'миң', 'миллион', 'миллиард', 'триллион']

    if num == 0:
        return 'ноль'

    def convert_three_digits(n):
        if n == 0:
            return ''
        elif n < 10:
            return ones[n]
        elif n < 100:
            word = tens[n // 10] + ' ' + ones[n % 10]
            return word.strip()
        else:
            word = ones[n // 100] + ' жүз ' + convert_three_digits(n % 100)
            return word.strip()

    def convert(n, index):
        if n == 0:
            return ''
        elif n < 1000:
            return convert_three_digits(n)
        else:
            word = convert_three_digits(n // 1000) + ' ' + scales[index] + ' ' + convert(n % 1000, index - 1)
            return word.strip()

    return convert(num, len(str(num)) // 3).strip()

def convert_to_phonetic(text, language):
    # Convert numbers to words
    if language == 'eng':
        text = re.sub(r'\d+', lambda x: num2words(int(x.group(0)), lang='en'), text)
    elif language == 'rus':
        text = re.sub(r'\d+', lambda x: num2words(int(x.group(0)), lang='ru'), text)
    elif language == 'kir':
        text = re.sub(r'\d+', lambda x: kyrgyz_num2words(int(x.group(0))), text)

    # Define phonetic spellings for capital letters
    phonetic_spellings = {
        'eng': {
            'A': '  ay  ', 'B': '  bee  ', 'C': '  see  ', 'D': '  dee  ', 'E': '  ee  ', 'F': '  ef  ',
            'G': '  gee  ', 'H': '  aitch  ', 'I': '  eye  ', 'J': '  jay  ', 'K': '  kay  ',
            'L': '  el  ', 'M': '  em  ', 'N': '  en  ', 'O': '  oh  ', 'P': '  pee  ', 'Q': '  cue  ',
            'R': '  ar  ', 'S': '  ess  ', 'T': '  tee  ', 'U': '  you  ', 'V': '  vee  ',
            'W': '  double-you  ', 'X': '  ex  ', 'Y': '  why  ', 'Z': '  zed  '
        },
        'rus': {
            'A': 'а ', 'B': 'бэ ', 'C': 'цэ ', 'D': 'дэ ', 'E': 'э ', 
            'F': 'эф ', 'G': 'жэ ', 'H': 'эйч ', 'I': 'и ', 'J': 'джэй ',
            'K': 'кэй ', 'L': 'эль ', 'M': 'эм ', 'N': 'эн ', 'O': 'о ',
            'P': 'пэ ', 'Q': 'кью ', 'R': 'ар ', 'S': 'эс ', 'T': 'тэ ',
            'U': 'ю ', 'V': 'вэ ', 'W': 'дабльвэ ', 'X': 'экс ', 'Y': 'иай ', 'Z': 'зэд '
        },
        'kir': {
            'A': 'а ', 'B': 'бэ ', 'C': 'цэ ', 'D': 'дэ ', 'E': 'е ',
            'F': 'эф ', 'G': 'гэ ', 'H': 'ха ', 'I': 'и ', 'J': 'жэ ',
            'K': 'ка ', 'L': 'эл ', 'M': 'эм ', 'N': 'эн ', 'O': 'о ',
            'P': 'пэ ', 'Q': 'кү ', 'R': 'эр ', 'S': 'эс ', 'T': 'тэ ',
            'U': 'ү ', 'V': 'вэ ', 'W': 'дабл вэ ', 'X': 'экс ', 'Y': 'йэ ', 'Z': 'зэд '
        }
    }

    # Convert capital letters to phonetic spelling
    if language in phonetic_spellings:
        for letter, spelling in phonetic_spellings[language].items():
            text = re.sub(letter, spelling, text)
    
    return text

def log_phonetic_conversion(text, language, phonetic_text):
    with open('phonetic_conversion.log', 'a') as log_file:
        log_file.write(f"Input Text: {text}\n")
        log_file.write(f"Language: {language}\n")
        log_file.write(f"Phonetic Text: {phonetic_text}\n")
        log_file.write("-" * 50 + "\n")

# tts/utils.py

def generate_audio(text, language, is_predefined=False):
    phonetic_text = convert_to_phonetic(text, language)
    log_phonetic_conversion(text, language, phonetic_text)

    model = VitsModel.from_pretrained(f"facebook/mms-tts-{language}")
    model.config.speaking_rate = 0.1
    model.config.noise_scale = 0.667
    model.config.noise_scale_w = 0.8

    tokenizer = AutoTokenizer.from_pretrained(f"facebook/mms-tts-{language}")

    inputs = tokenizer(phonetic_text, return_tensors="pt")
    inputs = {k: v.to(torch.long) for k, v in inputs.items()}  # Convert input tensors to Long

    with torch.no_grad():
        output = model(**inputs).waveform

    output = output.squeeze()
    
    # Use the first 20 characters of the text as the file name
    file_name = f"{text[:20]}_{language}.wav"
    if is_predefined:
        audio_folder = os.path.join(settings.MEDIA_ROOT, settings.PREDEFINED_AUDIO_FOLDER)
    else:
        audio_folder = os.path.join(settings.MEDIA_ROOT, settings.DYNAMIC_AUDIO_FOLDER)
    os.makedirs(audio_folder, exist_ok=True)  # Create the directory if it doesn't exist
    file_path = os.path.join(audio_folder, file_name)
    scipy.io.wavfile.write(file_path, rate=model.config.sampling_rate, data=output.float().numpy())

    return file_name

def combine_audio_files(template, predefined_files, dynamic_files, language):
    combined_audio = AudioSegment.empty()
    
    # Parse the template and build the audio segments list
    audio_segments = []
    template_parts = re.split(r'(\[[^\]]+\])', template)
    predefined_idx = 0
    dynamic_idx = 0
    
    for part in template_parts:
        if part.startswith('['):
            # Add the corresponding dynamic file
            placeholder = part[1:-1]
            dynamic_file = next((file for file in dynamic_files if placeholder in file), None)
            if dynamic_file:
                audio_path = os.path.join(settings.MEDIA_ROOT, settings.DYNAMIC_AUDIO_FOLDER, dynamic_file)
                
                if os.path.exists(audio_path):
                    audio = AudioSegment.from_wav(audio_path)
                    audio_segments.append(audio)
                    dynamic_idx += 1
                else:
                    logging.warning(f"Dynamic audio file not found: {audio_path}")
            else:
                logging.warning(f"No dynamic audio file found for placeholder: {placeholder}")
        else:
            # Add the corresponding predefined file
            if predefined_idx < len(predefined_files):
                audio_file = predefined_files[predefined_idx]
                audio_path = os.path.join(settings.MEDIA_ROOT, settings.PREDEFINED_AUDIO_FOLDER, audio_file)

                if os.path.exists(audio_path):
                    audio = AudioSegment.from_wav(audio_path)
                    audio_segments.append(audio)
                    predefined_idx += 1
                else:
                    logging.warning(f"Predefined audio file not found: {audio_path}")
    
    # Concatenate the audio segments in the correct order
    combined_audio = sum(audio_segments)

    file_name = f"announcement_{language}_combined.wav"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    combined_audio.export(file_path, format="wav")

    return file_name