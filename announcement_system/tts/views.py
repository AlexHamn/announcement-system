# tts/views.py

from django.shortcuts import render
from django.conf import settings
from .utils import generate_audio

def generate_announcement_audio(request):
    message = request.session.get('message', '')
    message_ru = request.session.get('message_ru', '')
    message_kg = request.session.get('message_kg', '')

    audio_files = []
    audio_files.append(generate_audio(message, 'eng'))
    audio_files.append(generate_audio(message_ru, 'rus'))
    audio_files.append(generate_audio(message_kg, 'kir'))

    context = {
        'audio_files': audio_files,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'tts/audio.html', context)

def test_view(request):
    return render(request, 'tts/test.html')