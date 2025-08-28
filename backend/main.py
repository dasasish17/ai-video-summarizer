from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create FastAPI application instance
app = FastAPI(
    title="AI Video Summarizer API",
    description="API for AI-powered video summarization and indexing",
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
        "timestamp": "2025-08-28T17:32:00Z",
        "service": "ai-video-summarizer",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

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
