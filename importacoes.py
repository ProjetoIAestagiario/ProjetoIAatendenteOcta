try:
    import pyttsx3
    import speech_recognition as sr
    import pyaudio
    import json
    import time
    import random
    import requests
    from flask import Flask, request, jsonify
except ImportError as e:
    print(f'Erro ao importar a biblioteca: {e}')
