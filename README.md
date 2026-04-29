# AI Digital Product Automation System

**AI-powered automation system to create premium digital products using 100% open-source models.**

## 🎯 What This Does

This system **fully automates** the creation of high-quality digital products:

### **Three Product Types:**
1. **eBooks** (20 pages max) - Custom-designed PDFs with professional branding
2. **Digital Assets** - Templates, step-by-step plans, plug-and-play solutions, mini tools
3. **Video Courses** - 1-hour auto-produced courses with voiceovers and captions

### **Complete Automation Pipeline:**
```
Internet Research → Market Analysis → Idea Generation → Planning → 
Content Creation → Professional Design → Quality Assurance → Delivery
```

## ✨ Key Features

✅ **100% Open-Source Models**
- Mistral 7B / Llama 2 for LLM
- Sentence Transformers for embeddings
- Stable Diffusion for images
- FFmpeg for video processing
- No proprietary API costs

✅ **Data-Driven Creation**
- Internet research for each idea
- Market gap analysis
- Keyword research
- Competitor analysis
- Problem identification from real discussions

✅ **Premium Quality (Not Generic)**
- Custom-branded PDF designs
- Professional content creation
- Unique angles based on market research
- Quality assurance gates

✅ **Fully Automated**
- Zero manual intervention
- Parallel batch processing
- Automatic quality checks
- Error recovery

✅ **Production-Ready**
- Docker containerization
- Database persistence
- Task queue management
- REST API
- Comprehensive logging

## 🚀 Quick Start

### **Prerequisites**
- Docker & Docker Compose
- Git
- 4GB RAM minimum
- 20GB storage for models

### **1. Clone Repository**
```bash
git clone https://github.com/rameesaq11/ai-digital-product-automation.git
cd ai-digital-product-automation
```

### **2. Start Services**
```bash
docker-compose up -d
```

This will:
- ✅ Download Mistral 7B model (~4GB)
- ✅ Start Ollama server
- ✅ Initialize PostgreSQL database
- ✅ Start Redis cache
- ✅ Launch FastAPI server
- ✅ Start Celery workers

### **3. Create Your First Product**
```bash
python main.py
```

### **4. Access Dashboard**
- **API Docs**: http://localhost:8000/docs
- **Celery Monitoring**: http://localhost:5555

## 📦 What's Included

### **Core Modules**
```
core/
├── llm_engine.py              # Ollama integration
├── idea_generator.py          # AI idea generation
├── market_research.py         # Internet research & analysis
└── problem_identifier.py      # Problem finding

design_engine/
├── ebook_designer.py          # Custom PDF design
├── template_generator.py      # Excel templates
└── branding.py                # Brand consistency

content_generation/
├── digital_asset_builder.py   # Plans, templates, tools
├── script_writer.py           # Video scripts
├── voice_generator.py         # Voiceovers
└── video_processor.py         # Video editing

orchestration/
├── workflow_engine.py         # Complete automation
├── task_manager.py            # Celery tasks
└── quality_gates.py           # QA checks

api/
├── product_api.py             # REST endpoints
└── webhooks.py                # Event listeners
```

## 🔧 Configuration

Edit `config/config.yaml` to customize:

```yaml
ollama:
  models:
    primary: mistral          # or llama2, neural-chat
    temperature: 0.7

quality:
  min_uniqueness_score: 0.85
  max_plagiarism: 5

content:
  ebook:
    max_pages: 20
    sections: 8
  video_course:
    duration_minutes: 60
```

## 📚 Usage Examples

### **Create an eBook**
```python
from orchestration.workflow_engine import ProductAutomationWorkflow

workflow = ProductAutomationWorkflow()
result = await workflow.execute(
    niche='Digital Marketing',
    product_type='ebook',
    quality_level='premium'
)

print(f"eBook created: {result['product_path']}")
```

### **Create a Digital Asset**
```python
result = await workflow.execute(
    niche='E-commerce',
    product_type='digital_asset',
    quality_level='premium'
)

print(f"Asset created: {result['product_path']}")
```

### **Create a Video Course**
```python
result = await workflow.execute(
    niche='Python Programming',
    product_type='video_course',
    quality_level='premium'
)

print(f"Video course created: {result['product_path']}")
```

## 🏗️ Architecture

### **Service Stack**
```
┌─────────────────────────────────────┐
│         FastAPI REST API            │
│     (Port 8000, Swagger UI)         │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│    Workflow Orchestration Engine    │
│      (6-Phase Automation)           │
└────┬───────────────────────────┬────┘
     ↓                           ↓
┌─────────────────┐     ┌──────────────────┐
│ Celery Workers  │     │  PostgreSQL DB   │
│  (Async Tasks)  │     │ (Persistence)    │
└────────┬────────┘     └──────────────────┘
         ↓
┌─────────────────────────────────────┐
│    Redis Cache & Task Queue         │
└────────────────┬────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Ollama Server (Local LLM Models)   │
│  - Mistral 7B                       │
│  - CodeLlama                        │
│  - Embeddings                       │
└─────────────────────────────────────┘
```

## 📊 Technology Stack

| Component | Technology |
|-----------|------------|
| **LLM** | Mistral 7B / Llama 2 (via Ollama) |
| **Embeddings** | Sentence Transformers |
| **Web Scraping** | BeautifulSoup, Selenium, Requests |
| **PDF Design** | ReportLab, WeasyPrint |
| **Templates** | OpenPyxl, CSV |
| **Video** | FFmpeg, OpenCV, MoviePy |
| **TTS** | Pyttsx3, Glow-TTS |
| **Backend** | FastAPI, Uvicorn |
| **Tasks** | Celery + Redis |
| **Database** | PostgreSQL |
| **Container** | Docker & Docker Compose |

## 🎯 Workflow Phases

### **Phase 1: Research**
- Internet research using open sources
- Keyword analysis
- Trend detection
- Competitor analysis
- Problem identification

### **Phase 2: Ideation**
- AI generates 5-10 unique ideas
- Market demand scoring
- Idea ranking
- Best idea selection

### **Phase 3: Planning**
- Content structure design
- Outline generation
- Resource planning
- Quality standards definition

### **Phase 4: Content Creation**
- AI writes premium content
- Multiple generation rounds
- Quality refinement
- Research-backed claims

### **Phase 5: Production**
- **eBooks**: Custom PDF design with branding
- **Assets**: Template/tool generation
- **Video**: Screen recording, voiceovers, editing

### **Phase 6: QA**
- Uniqueness checking
- Plagiarism detection
- Readability assessment
- Fact verification
- SEO optimization

## 🔒 Security & Privacy

✅ All processing is **local** (no data sent to external APIs)
✅ Models run on **your machine**
✅ Database is **encrypted**
✅ No telemetry or tracking
✅ Full control over your data

## 📈 Scaling

To scale for production:

```bash
# Increase Celery workers
docker-compose up -d --scale worker=4

# Use GPU support
docker-compose -f docker-compose.gpu.yml up -d

# Deploy to cloud
docker push rameesaq11/ai-digital-product-automation
```

## 🐛 Troubleshooting

### **Ollama model not downloading**
```bash
# Manually pull model
docker exec ollama ollama pull mistral
```

### **Out of memory**
```bash
# Reduce model size in config.yaml
models:
  primary: mistral  # Use smaller models
  embeddings: all-MiniLM-L6-v2
```

### **Check logs**
```bash
docker-compose logs -f
```

## 📝 Configuration Files

- `config/config.yaml` - Main configuration
- `config/llm_models.yaml` - Model settings
- `docker-compose.yml` - Service definitions
- `requirements.txt` - Python dependencies

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional open-source models
- More template types
- Enhanced video editing
- Additional data sources

## 📄 License

MIT License - Feel free to use commercially

## 🚀 Get Started Now

```bash
git clone https://github.com/rameesaq11/ai-digital-product-automation.git
cd ai-digital-product-automation
docker-compose up -d
python main.py
```

**Your AI-powered digital product automation system is ready!** ✨

---

**Questions?** Open an issue on GitHub.
