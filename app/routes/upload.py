from fastapi import APIRouter, UploadFile, File
from app.services.pdf_parser import extract_text_from_pdf
from app.services.chunker import chunk_text
from app.services.vector_store import store_chunks
import os
import shutil

# Create router object
router = APIRouter()

# Create uploads folder if it doesn't exist
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload PDF file endpoint
    """

    # Check if uploaded file is PDF
    if not file.filename.endswith(".pdf"):
        return {
            "status": "error",
            "message": "Only PDF files are allowed"
        }

    # Create file path
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from uploaded PDF
    extracted_text = extract_text_from_pdf(file_path)

   # Create chunks from extracted text
    chunks = chunk_text(extracted_text)

    # Store chunks in vector database
    stored_chunks = store_chunks(chunks)

    # Return response
    return {
        "filename": file.filename,
        "status": "uploaded successfully",
        "total_chunks": len(chunks),
        "stored_chunks": stored_chunks,
        "first_chunk": chunks[0]
    }