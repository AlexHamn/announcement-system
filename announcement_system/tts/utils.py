# tts/utils.py

import os
from django.conf import settings
from transformers import VitsModel, AutoTokenizer
import torch
import scipy
import re
from num2words import num2words

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
            'А': 'а ', 'Б': 'бэ ', 'В': 'вэ ', 'Г': 'гэ ', 'Д': 'дэ ', 'Е': 'е ', 'Ё': 'ё ',
            'Ж': 'жэ ', 'З': 'зэ ', 'И': 'и ', 'Й': 'и краткое ', 'К': 'ка ', 'Л': 'эль ',
            'М': 'эм ', 'Н': 'эн ', 'О': 'о ', 'П': 'пэ ', 'Р': 'эр ', 'С': 'эс ', 'Т': 'тэ ',
            'У': 'у ', 'Ф ': 'эф ', 'Х': 'ха ', 'Ц': 'цэ ', 'Ч': 'че ', 'Ш': 'ша ', 'Щ': 'ща ',
            'Ъ': 'твёрдый знак ', 'Ы': 'ы ', 'Ь': 'мягкий знак ', 'Э': 'э ', 'Ю': 'ю ', 'Я': 'я '
        },
        'kir': {
            'А': 'а ', 'Б': 'бе ', 'В': 'ве ', 'Г': 'ге ', 'Д': 'де ', 'Е': 'е ', 'Ё': 'ё ',
            'Ж': 'же ', 'З': 'зе ', 'И': 'и ', 'Й': 'й ', 'К': 'ка ', 'Л': 'эль ', 'М': 'эм ',
            'Н': 'эн ', 'Ң': 'ң ', 'О': 'о ', 'Ө': 'өү', 'П': 'пе', 'Р': 'эр', 'С': 'эс', 'Т': 'те',
            'У': 'у', 'Ү': 'үү', 'Ф': 'эф ', 'Х': 'ха', 'Ц': 'це', 'Ч': 'че', 'Ш': 'ше', 'Щ': 'ше',
            'Ъ': 'ъ', 'Ы': 'ы', 'Ь': 'ь ', 'Э': 'э', 'Ю': 'ю', 'Я': 'я'
        }
    }

    # Convert capital letters to phonetic spelling
    if language in phonetic_spellings:
        for letter, spelling in phonetic_spellings[language].items():
            text = re.sub(letter, spelling, text)
    
    return text

def log_phonetic_conversion(text, language, phonetic_text):
    with open('phonetic_conversion.log', 'a', encoding='utf-8') as log_file:
        log_file.write(f"Input Text: {text}\n")
        log_file.write(f"Language: {language}\n")
        log_file.write(f"Phonetic Text: {phonetic_text}\n")
        log_file.write("-" * 50 + "\n")

def generate_audio(text, language):
    phonetic_text = convert_to_phonetic(text, language)
    log_phonetic_conversion(text, language, phonetic_text)

    model = VitsModel.from_pretrained(f"facebook/mms-tts-{language}")
    model.config.speaking_rate = 0.1
    model.config.noise_scale = 0.667
    model.config.noise_scale_w = 0.8

    tokenizer = AutoTokenizer.from_pretrained(f"facebook/mms-tts-{language}")

    inputs = tokenizer(phonetic_text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform

    output = output.squeeze()

    file_name = f"announcement_{language}.wav"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    scipy.io.wavfile.write(file_path, rate=model.config.sampling_rate, data=output.float().numpy())

    return file_name