#!/usr/bin/env python3
"""Generate natural Bengali neural TTS clips (Edge Nabanita) for the deck."""
import asyncio
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audio" / "bn"
VOICE = "bn-BD-NabanitaNeural"
RATE = "-10%"
PITCH = "+4Hz"

CLIPS = {
    "ivr-0": "কৃষি বিলে আপনাকে স্বাগতম। আমি আপনার সহকারী।",
    "ivr-1": "সংযোগ হয়ে গেছে। কৃষি বিল চালু আছে।",
    "ivr-2": "ধান নির্বাচন হয়েছে। এখন পরিমাণ লিখুন।",
    "ivr-3": "দাম ঠিক হয়েছে। মোট দুই হাজার একশো টাকা।",
    "ivr-4": "ক্রেতার নম্বর দিন। শেষে হ্যাশ চাপুন।",
    "ivr-5": "চালান পাঠানো হয়েছে। রসিদ নম্বর কেবি আট আট চার দুই। রহিমের ফোনে মেসেজ চলে গেছে।",
    "ivr-6": "লেনদেন শেষ। আজকের মতো ধন্যবাদ, আবার আসবেন।",
    "trail-0": "গেট তিনে ক্যামেরা মুখ খুঁজছে।",
    "trail-1": "ছবি থেকে স্বাক্ষর তৈরি হয়েছে। জাতীয় তালিকায় খোঁজ চলছে।",
    "trail-2": "মিল পেয়েছি। আনোয়ার হোসেন। নির্ভুলতা ninety-four শতাংশ।",
    "cue-star": "স্টার",
    "cue-2": "দুই",
    "cue-4": "চার",
    "cue-7": "সাত",
    "cue-hash": "হ্যাশ",
    "cue-1": "এক",
    "cue-5": "পাঁচ",
    "cue-0": "শূন্য",
    "sync-1-0": "এখন ডায়াল করুন।",
    "sync-1-1": "স্টার।",
    "sync-1-2": "দুই।",
    "sync-1-3": "চার।",
    "sync-1-4": "সাত।",
    "sync-1-5": "হ্যাশ।",
    "sync-1-6": "সংযোগ হয়ে গেছে। কৃষি বিল চালু আছে।",
    "sync-2-0": "ধান নির্বাচনে এক চাপুন।",
    "sync-3-0": "পরিমাণ পঞ্চাশ কেজি।",
    "sync-3-1": "নিশ্চিত করতে, হ্যাশ।",
    "sync-4-0": "প্রতি কেজি বিয়ালিশ টাকা।",
    "sync-4-1": "নিশ্চিত, হ্যাশ।",
    "sync-5-0": "ক্রেতার মোবাইল নম্বর লিখুন।",
    "sync-5-1": "নম্বর লেখা হয়েছে। নিশ্চিত করতে, হ্যাশ।",
    "sync-6-0": "চালান পাঠাতে চাপুন",
    "sync-6-1": "হ্যাশ।",
}

# Always rewrite these (script/dialogue changes)
FORCE = {
    "sync-2-0", "sync-3-0", "sync-3-1", "sync-4-0", "sync-4-1", "sync-5-1",
}


async def one(name: str, text: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    mp3 = OUT / f"{name}.mp3"
    if mp3.exists() and mp3.stat().st_size > 500 and name not in FORCE:
        return
    communicate = __import__("edge_tts").Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(str(mp3))
    print("wrote", mp3.name)


async def main() -> None:
    try:
        import edge_tts  # noqa: F401
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts", "-q"])
    for name, text in CLIPS.items():
        await one(name, text)
    manifest = {k: f"audio/bn/{k}.mp3" for k in CLIPS}
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print("manifest", OUT / "manifest.json")


if __name__ == "__main__":
    asyncio.run(main())
