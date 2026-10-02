# 📚 StudyGenie AI

An AI-powered web tool that converts your PDF notes into flashcards and quizzes instantly.

## What it does

Upload any PDF — typed or handwritten/scanned — and StudyGenie AI will:
1. Extract the text from it (using OCR if it's a scanned document)
2. Generate 5 flashcards (Question & Answer format)
3. Generate a 5-question quiz with multiple choice options
4. Let you choose the output language (English or Hindi)

## Features

- 📄 Supports both typed PDFs and scanned/image-based PDFs (via OCR)
- 🗂️ Interactive flashcards — click to flip and reveal the answer
- 📝 Interactive quiz — instant feedback with a live score
- 🌐 Language selection (English / Hindi)
- 🎨 Clean, custom-designed interface

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini API (gemini-flash-latest)
- **PDF Reading:** PyPDF2
- **OCR (for scanned PDFs):** Tesseract OCR + PyMuPDF + Pillow
- **Frontend:** HTML, CSS, JavaScript

## How to Run Locally

1. Clone this repository