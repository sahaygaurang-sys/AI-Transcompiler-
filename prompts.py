def build_translation_prompt(code: str, source_lang: str, target_lang: str) -> str:
    return f"""
You are an expert code transcompiler.

Task:
Translate the following {source_lang} code into correct {target_lang} code.

Strict rules:
- Preserve the original logic exactly
- Output only the translated code
- Do not add explanations
- Do not add markdown
- Do not wrap the answer in triple backticks
- Use idiomatic {target_lang} syntax
- If the input has tiny mistakes, correct them before translating
- Keep the output complete and runnable whenever possible

Source code:
{code}
""".strip()