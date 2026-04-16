import os
import ast
import re
from huggingface_hub import InferenceClient
from prompts import build_translation_prompt


def get_client():
    api_key = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        raise ValueError(
            "HF_TOKEN is not set. Please set it before running the app."
        )
    return InferenceClient(token=api_key)


def clean_output(text: str) -> str:
    if not text:
        return ""

    cleaned = text.strip()

    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```[a-zA-Z]*\n?", "", cleaned)
        cleaned = re.sub(r"\n?```$", "", cleaned)

    cleaned = cleaned.strip()

    prefixes_to_remove = [
        "Here is the translated code:",
        "Translated code:",
        "Output:",
    ]

    for prefix in prefixes_to_remove:
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix):].strip()

    return cleaned


def translate_code(code: str, source_lang: str, target_lang: str, model_name: str) -> str:
    prompt = build_translation_prompt(
        code=code,
        source_lang=source_lang,
        target_lang=target_lang,
    )

    try:
        client = get_client()
        response = client.chat_completion(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        return clean_output(response.choices[0].message.content)
    except Exception as e:
        return f"Error during translation: {str(e)}"


def validate_python_code(code: str):
    if code.startswith("Error during translation:"):
        return False, code

    try:
        ast.parse(code)
        return True, "Valid Python syntax."
    except Exception as e:
        return False, f"Invalid Python syntax: {str(e)}"


def validate_java_code(code: str):
    if code.startswith("Error during translation:"):
        return False, code

    java_signals = [
        ";",
        "{",
        "}",
        "class ",
        "public ",
        "static ",
        "System.out.println",
    ]

    signal_count = sum(1 for token in java_signals if token in code)

    if signal_count >= 3:
        return True, "Java structure looks reasonable."
    return False, "Java code could not be confidently validated. Please check braces, class structure, and semicolons manually."