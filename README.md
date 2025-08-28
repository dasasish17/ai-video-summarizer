# AI Video Summarizer

AI-powered video summarizer and indexer that generates concise summaries, searchable transcripts, and highlights from uploaded videos using advanced speech-to-text and large language models.

## 🚀 Features

- **Video Upload & Processing**: Support for multiple video formats with drag-and-drop interface
- **Speech-to-Text Conversion**: High-accuracy transcription using Whisper or AssemblyAI
- **AI-Powered Summarization**: Generate concise summaries using GPT-4 or Claude
- **Searchable Transcripts**: Full-text search across video transcripts
- **Highlight Extraction**: Automatically identify key moments and highlights
- **Multi-format Output**: Export summaries in various formats (PDF, JSON, TXT)
- **Real-time Progress**: Live updates during processing
- **Responsive Design**: Works seamlessly on desktop and mobile

## 🏗️ Project Structure

```
ai-video-summarizer/
├── backend/          # API and AI processing components
├── frontend/         # React-based web interface
├── docs/            # Comprehensive project documentation
├── .gitignore       # Python gitignore template
├── LICENSE          # MIT license
└── README.md        # This file
```

## 🛠️ Technology Stack

### Backend
- Python 3.8+
- FastAPI/Flask for API framework
- Whisper/AssemblyAI for speech-to-text
- OpenAI GPT/Claude for summarization
- PostgreSQL/MongoDB for data storage
- Redis for caching
- Celery for background processing

### Frontend
- React 18+ with TypeScript
- Next.js or Vite for build tooling
- Tailwind CSS for styling
- React Query for state management
- Video.js for video playback

## 📚 Documentation

For detailed information, please refer to our comprehensive documentation:

- [Backend Documentation](./backend/README.md) - API and processing components
- [Frontend Documentation](./frontend/README.md) - Web interface details
- [Full Documentation](./docs/README.md) - Complete project documentation

## 🚀 Quick Start

*Coming soon - Setup and installation instructions will be added as development progresses.*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please check out our [Contributing Guidelines](./docs/README.md#developer-documentation) for details.

## 📧 Contact

For questions or support, please open an issue on this repository.
