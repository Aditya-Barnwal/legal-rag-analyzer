import pymupdf
import os

def extract_text_from_pdf(pdf_path):
    doc=pymupdf.Document(pdf_path)
    text=""
    for page in doc:
       text+=page.get_text()
    return text

def process_all_pdfs(raw_folder="data/raw", processed_folder="data/processed"):
    os.makedirs(processed_folder, exist_ok=True)
    for filename in os.listdir(raw_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path=os.path.join(raw_folder, filename)
            print(f"📄Processing: {filename}")
            text=extract_text_from_pdf(pdf_path)

            txt_filename=filename.replace(".pdf", ".txt")
            txt_path=os.path.join(processed_folder, txt_filename)
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"✅ Saved extracted text to {txt_path}")
