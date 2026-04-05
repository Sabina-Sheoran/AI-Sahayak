"""
SabbiAI TTS API - Uses Microsoft Edge TTS for high-quality Hindi speech
Free, fast, supports Hindi female voice (Swara)
"""

import asyncio
import base64
import os
from pathlib import Path
from edge_tts import Communicate

TEMP_DIR = Path("temp_audio")
TEMP_DIR.mkdir(exist_ok=True)

VOICE_HINDI_FEMALE = "hi-IN-SwaraNeural"
VOICE_HINDI_MALE = "hi-IN-MadhurNeural"

_temp_files = []


def clean_old_files():
    """Remove old temp audio files"""
    import time

    now = time.time()
    for f in TEMP_DIR.glob("*.mp3"):
        try:
            if now - f.stat().st_mtime > 300:
                f.unlink()
        except:
            pass


async def generate_speech_async(
    text: str, voice: str = VOICE_HINDI_FEMALE, rate: str = "+0%", pitch: str = "+0Hz"
) -> bytes:
    """Generate speech audio from text"""
    clean_old_files()

    tts = Communicate(text, voice, rate=rate, pitch=pitch)
    audio_data = b""
    async for chunk in tts.stream():
        if chunk:
            if isinstance(chunk, bytes):
                audio_data += chunk
            elif isinstance(chunk, dict) and "data" in chunk:
                audio_data += chunk["data"]
    return audio_data


def generate_speech(
    text: str, voice: str = VOICE_HINDI_FEMALE, rate: str = "+0%", pitch: str = "+0Hz"
) -> bytes:
    """Sync wrapper for generate_speech_async"""
    return asyncio.run(generate_speech_async(text, voice, rate, pitch))


def generate_speech_base64(
    text: str, voice: str = VOICE_HINDI_FEMALE, rate: str = "+0%", pitch: str = "+0Hz"
) -> str:
    """Generate speech and return as base64 string"""
    audio = generate_speech(text, voice, rate, pitch)
    return base64.b64encode(audio).decode("utf-8")


async def generate_speech_file_async(
    text: str,
    filename: str,
    voice: str = VOICE_HINDI_FEMALE,
    rate: str = "+0%",
    pitch: str = "+0Hz",
) -> str:
    """Generate speech and save to file, return file path"""
    clean_old_files()

    filepath = TEMP_DIR / filename
    tts = Communicate(text, voice, rate=rate, pitch=pitch)
    await tts.save(str(filepath))

    _temp_files.append(str(filepath))
    return str(filepath)


async def list_available_voices():
    """List all available Hindi voices"""
    from edge_tts import list_voices

    voices = await list_voices()
    hindi = [v for v in voices if "hi-IN" in v["Locale"]]
    return hindi


if __name__ == "__main__":
    print("Testing edge-tts...")

    test_text = "नमस्ते भाई, मैं आपकी मदद करूँगी। पी एम किसान योजना के बारे में बताइए।"

    print("Generating female voice...")
    audio = asyncio.run(generate_speech_async(test_text, VOICE_HINDI_FEMALE))
    print(f"Generated {len(audio)} bytes")

    with open("test_female.mp3", "wb") as f:
        f.write(audio)
    print("Saved test_female.mp3")

    print("\nListing Hindi voices:")
    voices = asyncio.run(list_available_voices())
    for v in voices:
        print(f"  {v['ShortName']} - {v['FriendlyName']}")
