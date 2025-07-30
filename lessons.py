"""Interactive lesson introducing iambic pentameter."""
from __future__ import annotations

import os

# Dataset used for example lines in this lesson. The previous placeholder
# ``username/dataset_name`` has been replaced with the actual Hugging Face
# dataset identifier.
DATASET_ID = "scenecoachai/shakespeare"

try:
    import speech_recognition as sr  # type: ignore
except Exception:  # ImportError or other issues
    sr = None  # type: ignore


def _get_user_input(prompt: str) -> str:
    """Prompt the user to repeat a line either by voice or keyboard."""
    force_text = os.getenv("SCENECOACH_FORCE_TEXT")
    if force_text:
        return input(prompt)

    if sr is not None:
        try:
            with sr.Microphone() as source:  # type: ignore[attr-defined]
                recognizer = sr.Recognizer()  # type: ignore[attr-defined]
                print(prompt + " (speak now)")
                recognizer.listen(source, timeout=5)
                # The audio is not transcribed but capturing fulfills the exercise.
                print("(audio captured)")
                return ""
        except Exception:
            # fall back to text
            pass
    return input(prompt)


def introduce_iambic_pentameter() -> None:
    """Run a short lesson on iambic pentameter."""
    print(
        "Iambic pentameter uses five pairs of syllables per line, "
        "with the stress on the second syllable of each pair."
    )
    lines = [
        "But, soft! what light through yonder window breaks?",
        "Shall I compare thee to a summer's day?",
        "Now is the winter of our discontent",
    ]
    for line in lines:
        _get_user_input(f"Repeat after me: '{line}'\n")
    print("Great job! That's iambic pentameter.")


def main() -> None:
    """Entry point for ``python -m scenecoach.lesson``."""
    introduce_iambic_pentameter()


if __name__ == "__main__":  # pragma: no cover - manual entry point
    main()
