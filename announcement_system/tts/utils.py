import os
from django.conf import settings
from transformers import VitsModel, AutoTokenizer
import torch
import scipy

def generate_audio(text, language):
    model = VitsModel.from_pretrained(f"facebook/mms-tts-{language}")
    model.config.speaking_rate = 0.1
    model.config.noise_scale = 0.667
    model.config.noise_scale_w = 0.8

    tokenizer = AutoTokenizer.from_pretrained(f"facebook/mms-tts-{language}")

    inputs = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**inputs).waveform

    output = output.squeeze()

    file_name = f"announcement_{language}.wav"
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    scipy.io.wavfile.write(file_path, rate=model.config.sampling_rate, data=output.float().numpy())

    return file_name