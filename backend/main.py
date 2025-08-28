from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil
from pathlib import Path
from typing import List
from dotenv import load_dotenv
import datetime

# Load environment variables from .env file
load_dotenv()

# Create uploads directory if it doesn't exist
UPLOADS_DIR = Path("uploads")
UPLOADS_DIR.mkdir(exist_ok=True)

# Allowed video file extensions
ALLOWED_EXTENSIONS = {".mp4", ".mov", ".avi"}
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB limit

# Response models
class UploadResponse(BaseModel):
    filename: str
    status: str
    message: str
    file_size: int
    upload_time: str

# Create FastAPI application instance
app = FastAPI(
    title="AI Video Summarizer API",
    description="API for AI-powered video summarization and indexing with video upload functionality",
    version="1.0.0"
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    """
    Health check endpoint that returns API status and basic information.
    """
    return {
        "status": "healthy",
        "message": "AI Video Summarizer API is running",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/api/v1/health")
async def api_health():
    """
    Detailed health check endpoint for monitoring.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "service": "ai-video-summarizer",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

def validate_video_file(file: UploadFile) -> bool:
    """
    Validate uploaded file format and size.
    
    Args:
        file: Uploaded file object
        
    Returns:
        bool: True if file is valid, False otherwise
        
    Raises:
        HTTPException: If file validation fails
    """
    # Check file extension
    file_extension = Path(file.filename).suffix.lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file format. Allowed formats: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Check file size (this is a basic check, actual size validation happens during upload)
    if hasattr(file, 'size') and file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size allowed: {MAX_FILE_SIZE // (1024*1024)}MB"
        )
    
    return True

@app.post("/api/v1/upload", response_model=UploadResponse)
async def upload_video(
    file: UploadFile = File(..., description="Video file to upload (mp4, mov, avi)")
):
    """
    Upload and validate video files.
    
    This endpoint accepts video files in mp4, mov, or avi format,
    validates the file type and size, saves it to the local uploads/
    directory, and returns upload status information.
    
    Args:
        file: Video file to upload
        
    Returns:
        UploadResponse: Upload status and file information
        
    Raises:
        HTTPException: If file validation fails or upload error occurs
    """
    try:
        # Validate the uploaded file
        validate_video_file(file)
        
        # Generate unique filename to avoid conflicts
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_extension = Path(file.filename).suffix.lower()
        safe_filename = f"{timestamp}_{file.filename}"
        file_path = UPLOADS_DIR / safe_filename
        
        # Save the uploaded file
        file_size = 0
        with open(file_path, "wb") as buffer:
            # Read and write file in chunks to handle large files
            while chunk := await file.read(1024):
                file_size += len(chunk)
                buffer.write(chunk)
                
                # Check file size during upload
                if file_size > MAX_FILE_SIZE:
                    # Remove partially uploaded file
                    if file_path.exists():
                        file_path.unlink()
                    raise HTTPException(
                        status_code=413,
                        detail=f"File too large. Maximum size allowed: {MAX_FILE_SIZE // (1024*1024)}MB"
                    )
        
        # Return success response
        return UploadResponse(
            filename=safe_filename,
            status="success",
            message="Video file uploaded successfully",
            file_size=file_size,
            upload_time=datetime.datetime.utcnow().isoformat() + "Z"
        )
        
    except HTTPException:
        # Re-raise HTTP exceptions (validation errors)
        raise
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error during file upload: {str(e)}"
        )
    finally:
        # Ensure file handle is closed
        await file.close()

@app.get("/api/v1/uploads")
async def list_uploads():
    """
    List all uploaded video files.
    
    Returns:
        dict: List of uploaded files with metadata
    """
    try:
        files = []
        for file_path in UPLOADS_DIR.glob("*"):
            if file_path.is_file():
                stat = file_path.stat()
                files.append({
                    "filename": file_path.name,
                    "size": stat.st_size,
                    "created": datetime.datetime.fromtimestamp(stat.st_ctime).isoformat() + "Z",
                    "modified": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat() + "Z"
                })
        
        return {
            "status": "success",
            "count": len(files),
            "files": files
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error listing uploaded files: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    
    # Run the application with uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
