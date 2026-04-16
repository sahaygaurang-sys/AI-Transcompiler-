import streamlit as st
from translator import translate_code, validate_python_code, validate_java_code

st.set_page_config(page_title="AI Code Transcompiler", layout="wide")

st.title("AI Code Transcompiler")
st.write("Translate code between Python and Java using Hugging Face API.")

with st.sidebar:
    st.header("Settings")
    model_name = st.selectbox(
        "Hugging Face Model",
        ["meta-llama/Meta-Llama-3-8B-Instruct", "mistralai/Mistral-7B-Instruct-v0.3", "google/gemma-1.1-7b-it"],
        index=0
    )
    st.caption("Make sure HF_TOKEN is set in your environment.")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", ["Python", "Java"])

with col2:
    target_lang = st.selectbox("Target Language", ["Java", "Python"])

code_input = st.text_area("Paste your source code here", height=320)

translate_clicked = st.button("Translate")

if translate_clicked:
    if source_lang == target_lang:
        st.warning("Source and target languages must be different.")
    elif not code_input.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Translating with Hugging Face..."):
            translated_code = translate_code(
                code=code_input,
                source_lang=source_lang,
                target_lang=target_lang,
                model_name=model_name,
            )

        st.subheader("Translated Code")
        st.code(translated_code, language=target_lang.lower())

        st.subheader("Validation")

        if target_lang == "Python":
            is_valid, message = validate_python_code(translated_code)
            if is_valid:
                st.success(message)
            else:
                st.error(message)

        elif target_lang == "Java":
            is_valid, message = validate_java_code(translated_code)
            if is_valid:
                st.success(message)
            else:
                st.warning(message)

st.markdown("---")
st.subheader("Sample Inputs")

sample_python = """def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 5
print(factorial(num))
"""

sample_java = """public class Main {
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        int num = 5;
        System.out.println(factorial(num));
    }
}
"""

sample_col1, sample_col2 = st.columns(2)

with sample_col1:
    st.caption("Python Example")
    st.code(sample_python, language="python")

with sample_col2:
    st.caption("Java Example")
    st.code(sample_java, language="java")   