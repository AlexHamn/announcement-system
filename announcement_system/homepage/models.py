# homepage/models.py

from django.db import models
import re
from tts.utils import generate_audio
from django.conf import settings
import os
import logging

# Configure logging
log_file_path = os.path.join(settings.BASE_DIR, 'predefined_audio_generation.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    template = models.TextField()
    template_ru = models.TextField()
    template_kg = models.TextField()
    predefined_audio_files = models.JSONField(default=list, blank=True)  # Make the field optional

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        logging.info(f"Saving Subcategory instance: {self.name}")
        if not self.predefined_audio_files:
            self.predefined_audio_files = self.generate_predefined_audio_files()
        super().save(*args, **kwargs)

# homepage/models.py

    def generate_predefined_audio_files(self):
        predefined_audio_files = []

        for lang, template in [('eng', self.template), ('rus', self.template_ru), ('kir', self.template_kg)]:
            parts = re.split(r'(\[[^\]]+\])', template)
            for part in parts:
                if not part.startswith('[') and part.strip():
                    text = part.strip()
                    audio_file = f"{text[:20]}_{lang}.wav"
                    predefined_audio_folder = os.path.join(settings.MEDIA_ROOT, settings.PREDEFINED_AUDIO_FOLDER)
                    os.makedirs(predefined_audio_folder, exist_ok=True)  # Create the directory if it doesn't exist
                    audio_path = os.path.join(predefined_audio_folder, audio_file)
                    logging.info(f"Generating audio for text: {text}")
                    logging.info(f"Audio file: {audio_file}")
                    logging.info(f"Audio path: {audio_path}")
                    if not os.path.exists(audio_path):
                        audio_file = generate_audio(text, lang, is_predefined=True)
                        logging.info(f"Generated audio file: {audio_file}")
                    else:
                        logging.info(f"Audio file already exists: {audio_file}")
                    predefined_audio_files.append(os.path.join(settings.PREDEFINED_AUDIO_FOLDER, audio_file))

        return predefined_audio_files