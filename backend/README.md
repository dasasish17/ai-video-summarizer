# Backend

This directory contains the backend API and AI processing components for the AI Video Summarizer.

## Features

- Video upload and processing
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

- `GET /` - Health check endpoint
- `GET /api/v1/health` - Detailed health status

### Development

- The API runs with auto-reload enabled in development mode
- FastAPI provides automatic interactive documentation
- CORS is enabled for frontend integration

### Next Steps

- Add video upload endpoints
- Integrate speech-to-text services
- Implement AI summarization features
- Add database integration
- Set up background task processing
