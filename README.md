# 📚 StudyGenie AI

An AI-powered web tool that converts your PDF notes into flashcards and quizzes instantly.

## What it does

Upload any PDF — typed or handwritten/scanned — and StudyGenie AI will:
1. Extract the text from it (using OCR if it's a scanned document)
2. Generate 5 flashcards (Question & Answer format)
3. Generate a 5-question quiz with multiple choice options
4. Let you choose the output language (English or Hindi)

## Features

- Supports both typed PDFs and scanned/image-based PDFs (via OCR)
- Interactive flashcards — click to flip and reveal the answer
- Interactive quiz — instant feedback with a live score
- Language selection (English / Hindi)
- Clean, custom-designed interface

## Tech Stack

- Backend: Python, Flask
- AI: Google Gemini API (gemini-flash-latest)
- PDF Reading: PyPDF2
- OCR (for scanned PDFs): Tesseract OCR + PyMuPDF + Pillow
- Frontend: HTML, CSS, JavaScript

## How to Run Locally

Step 1: Clone this repository using git clone followed by the repository URL, then move into the folder using cd StudyGenie-AI

Step 2: Install the required Python libraries by running: pip install -r requirements.txt

Step 3: Install Tesseract OCR (needed for scanned PDF support). Download it from github.com/UB-Mannheim/tesseract/wiki, install it, and note the install path.

Step 4: Add your Gemini API key. Get a free key from aistudio.google.com/apikey, then open app.py and replace YOUR_GEMINI_API_KEY_HERE with your actual key.

Step 5: Run the app using the command: python app.py

Step 6: Open your browser and go to http://127.0.0.1:5000

## Future Improvements (Major Project Scope)

- User login and saved history
- Choice of number of flashcards/quiz questions
- Full chat-style interface
- Mobile app version

## Author

Shivam Shukla — 3rd Year, Computer Science / IT