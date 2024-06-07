# tts/views.py

from django.shortcuts import render
from django.conf import settings
from .utils import generate_audio, combine_audio_files
from homepage.models import Subcategory
import logging
import os

def generate_announcement_audio(request):
    subcategory_id = request.session.get('subcategory_id')
    subcategory = Subcategory.objects.get(id=subcategory_id)

    predefined_audio_files = subcategory.predefined_audio_files
    placeholders = request.session.get('placeholders', {})

    # Generate audio files for the dynamic parts
    dynamic_audio_files = []
    for placeholder, value in placeholders.items():
        for lang in ['eng', 'rus', 'kir']:
            audio_file_name = f"{value}_{lang}.wav"
            audio_file_path = os.path.join(settings.MEDIA_ROOT, settings.DYNAMIC_AUDIO_FOLDER, audio_file_name)

            if os.path.exists(audio_file_path):
                logging.info(f"Dynamic audio file already exists: {audio_file_name}")
                dynamic_audio_files.append(audio_file_name)
            else:
                logging.info(f"Generating audio for placeholder: {placeholder}, value: {value}, language: {lang}")
                dynamic_audio_file = generate_audio(value, lang, is_predefined=False)
                if dynamic_audio_file:
                    dynamic_audio_files.append(dynamic_audio_file)
                    logging.info(f"Generated dynamic audio file: {dynamic_audio_file}")
                    logging.info(f"Dynamic audio file path: {os.path.join(settings.MEDIA_ROOT, settings.DYNAMIC_AUDIO_FOLDER, dynamic_audio_file)}")

    combined_audio_files = []
    for lang, template in [('eng', subcategory.template), ('rus', subcategory.template_ru), ('kir', subcategory.template_kg)]:
        predefined_files = [file for file in predefined_audio_files if file.endswith(f'_{lang}.wav')]
        dynamic_files = [file for file in dynamic_audio_files if file.endswith(f'_{lang}.wav')]
        combined_audio = combine_audio_files(template, predefined_files, dynamic_files, lang, placeholders)
        if combined_audio:
            combined_audio_files.append(combined_audio)

    context = {
        'audio_files': [os.path.join(settings.MEDIA_URL, audio_file) for audio_file in combined_audio_files],
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'tts/audio.html', context)