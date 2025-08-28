# Backend

This directory contains the backend API and AI processing components for the AI Video Summarizer.

## Features

- Video upload and processing with format validation
- Speech-to-text conversion
- AI-powered summarization using large language models
- Transcript generation and searchable indexing
- Highlight extraction
- RESTful API endpoints

## Technology Stack

- Python 3.8+
- FastAPI for API framework
- Whisper/AssemblyAI for speech-to-text
- OpenAI GPT/Claude for summarization
- PostgreSQL/MongoDB for data storage
- Redis for caching
- Celery for background task processing

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file:**
   ```bash
   # Create a .env file in the backend directory
   touch .env
   ```
   
   Add the following environment variables to your `.env` file:
   ```env
   ENVIRONMENT=development
   API_HOST=0.0.0.0
   API_PORT=8000
   ```

### Running the Application

1. **Start the FastAPI server:**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Access the API:**
   - API Base URL: `http://localhost:8000`
   - Interactive API Documentation: `http://localhost:8000/docs`
   - Alternative API Documentation: `http://localhost:8000/redoc`

### Available Endpoints

#### Health Check Endpoints
- `GET /` - Basic health check endpoint
- `GET /api/v1/health` - Detailed health status with environment info

#### Video Upload Endpoints
- `POST /api/v1/upload` - Upload video files (mp4, mov, avi)
- `GET /api/v1/uploads` - List all uploaded video files

### Video Upload API

#### Upload Video File

**Endpoint:** `POST /api/v1/upload`

**Description:** Upload and validate video files. Accepts video files in mp4, mov, or avi format, validates the file type and size, saves it to the local uploads/ directory.

**Request:**
- **Method:** POST
- **Content-Type:** multipart/form-data
- **Body:** Form data with a file field containing the video file

**Supported Formats:**
- `.mp4` - MPEG-4 video files
- `.mov` - QuickTime video files
- `.avi` - Audio Video Interleave files

**File Size Limit:** 100MB maximum

**Response:**
```json
{
  "filename": "20250828_123456_example_video.mp4",
  "status": "success",
  "message": "Video file uploaded successfully",
  "file_size": 15728640,
  "upload_time": "2025-08-28T17:34:56.789Z"
}
```

**Error Responses:**
- `400 Bad Request` - Invalid file format
- `413 Payload Too Large` - File size exceeds 100MB limit
- `500 Internal Server Error` - Server error during upload

#### List Uploaded Files

**Endpoint:** `GET /api/v1/uploads`

**Description:** List all uploaded video files with metadata.

**Response:**
```json
{
  "status": "success",
  "count": 2,
  "files": [
    {
      "filename": "20250828_123456_example_video.mp4",
      "size": 15728640,
      "created": "2025-08-28T17:34:56.789Z",
      "modified": "2025-08-28T17:34:56.789Z"
    },
    {
      "filename": "20250828_124512_another_video.mov",
      "size": 23456789,
      "created": "2025-08-28T17:45:12.345Z",
      "modified": "2025-08-28T17:45:12.345Z"
    }
  ]
}
```

### Sample cURL Requests

#### Upload a Video File
```bash
# Upload a video file
curl -X POST "http://localhost:8000/api/v1/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/video.mp4"
```

#### List Uploaded Files
```bash
# List all uploaded files
curl -X GET "http://localhost:8000/api/v1/uploads" \
  -H "accept: application/json"
```

#### Health Check
```bash
# Basic health check
curl -X GET "http://localhost:8000/" \
  -H "accept: application/json"

# Detailed health check
curl -X GET "http://localhost:8000/api/v1/health" \
  -H "accept: application/json"
```

### Development

- The API runs with auto-reload enabled in development mode
- FastAPI provides automatic interactive documentation at `/docs`
- Alternative documentation is available at `/redoc`
- CORS is enabled for frontend integration
- Uploaded files are stored in the `uploads/` directory (created automatically)

### File Storage

- Uploaded files are saved to a local `uploads/` directory
- Files are given unique names with timestamp prefixes to avoid conflicts
- Original filenames are preserved with the timestamp prefix
- File metadata is tracked including size and creation/modification times

### Error Handling

- Comprehensive validation for file types and sizes
- Graceful error handling with descriptive error messages
- Proper HTTP status codes for different error scenarios
- File cleanup in case of upload failures

### Next Steps

- ✅ ~~Add video upload endpoints~~
- Integrate speech-to-text services
- Implement AI summarization features
- Add database integration for file metadata
- Set up background task processing
- Add user authentication and authorization
- Implement video processing pipeline
