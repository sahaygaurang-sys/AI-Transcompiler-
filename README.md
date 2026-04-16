# AI Code Transcompiler

A beginner-friendly Streamlit app that translates code between Python and Java using the Gemini API.

## Features

- Python to Java translation
- Java to Python translation
- Gemini API integration
- Python syntax validation
- Basic Java structure validation
- Simple Streamlit web interface

## Project Files

- `app.py` -> Streamlit frontend
- `translator.py` -> Gemini API logic and validation
- `prompts.py` -> Prompt template
- `requirements.txt` -> Python dependencies

## Setup

### 1. Create environment

Using conda:

```bash
conda create -n transcompiler python=3.10 -y
conda activate transcompiler
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Gemini API key

#### Windows CMD

```bash
set GEMINI_API_KEY=your_api_key_here
```

#### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### 4. Run the app

```bash
streamlit run app.py
```

## Deployment

You can deploy this app on Streamlit Community Cloud.

### Steps

1. Push the project to GitHub
2. Open Streamlit Community Cloud
3. Create a new app
4. Select your GitHub repository
5. Choose `app.py` as the entry file
6. Add `GEMINI_API_KEY` in the app secrets or environment settings
7. Deploy

## Notes

- The Java validation is heuristic only
- Python validation uses Python's AST parser
- Gemini may sometimes add small formatting differences, so always review the translated output