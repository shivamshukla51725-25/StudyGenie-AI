from flask import Flask, render_template, request
import PyPDF2
import google.generativeai as genai
import json
import pytesseract
import fitz  # PyMuPDF
from PIL import Image
import io

app = Flask(__name__)

# Agar "tesseract is not installed" error aaye, to neeche wali line mein
# apna sahi install path daalo (jo install ke time note kiya tha)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

model = genai.GenerativeModel("gemini-flash-latest")


def extract_text_normal(pdf_bytes):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_bytes))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def extract_text_ocr(pdf_bytes):
    text = ""
    pdf_doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    for page in pdf_doc:
        pix = page.get_pixmap(dpi=200)
        img_bytes = pix.tobytes("png")
        img = Image.open(io.BytesIO(img_bytes))
        text += pytesseract.image_to_string(img)
    return text


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    uploaded_file = request.files['pdf_file']
    selected_language = request.form.get('language', 'English')

    if uploaded_file.filename == '':
        return "<h2 style='color:red; text-align:center;'>Error: No file selected. Please choose a PDF and try again.</h2>"

    if not uploaded_file.filename.lower().endswith('.pdf'):
        return "<h2 style='color:red; text-align:center;'>Error: Invalid file type. Please upload a PDF file only.</h2>"

    try:
        pdf_bytes = uploaded_file.read()

        extracted_text = extract_text_normal(pdf_bytes)

        used_ocr = False
        if not extracted_text.strip():
            extracted_text = extract_text_ocr(pdf_bytes)
            used_ocr = True

        if not extracted_text.strip():
            return "<h2 style='color:red; text-align:center;'>Error: Could not read any text from this PDF, even with OCR. The image quality might be too low. Please try a clearer file.</h2>"

        extracted_text = extracted_text[:4000]

        prompt = f"""
        Read the following text and generate exactly 5 flashcards and 5 MCQ quiz questions.

        Text: {extracted_text}

        Respond ONLY with valid JSON in this exact structure, nothing else before or after:
        {{
          "flashcards": [
            {{"question": "...", "answer": "..."}}
          ],
          "quiz": [
            {{"question": "...", "options": ["A", "B", "C", "D"], "correct_answer": "A"}}
          ]
        }}

        Write everything in {selected_language} language only. Do not include markdown formatting like ```json, just raw JSON.
        """

        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]

        data = json.loads(raw_text)

        return render_template('result.html', flashcards=data['flashcards'], quiz=data['quiz'])

    except Exception as e:
        return f"<h2 style='color:red; text-align:center;'>Error: AI could not generate content. Reason: {str(e)}</h2>"


if __name__ == '__main__':
    app.run(debug=True)