"""
FastAPI - REST API Endpoints
"""

from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
import logging
from orchestration.task_manager import create_product_task

logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Digital Product Automation API",
    description="Create digital products using AI",
    version="1.0.0"
)


class ProductRequest(BaseModel):
    niche: str
    product_type: str  # 'ebook', 'digital_asset', 'video_course'
    quality_level: str = 'premium'


class ProductResponse(BaseModel):
    status: str
    product_type: str
    product_path: str
    quality_score: float
    niche: str


@app.get("/")
async def root():
    """API health check"""
    return {
        "status": "operational",
        "service": "AI Digital Product Automation",
        "version": "1.0.0"
    }


@app.post("/create-product")
async def create_product(request: ProductRequest, background_tasks: BackgroundTasks):
    """Create a digital product"""
    
    logger.info(f"Creating {request.product_type} for {request.niche}")
    
    # Queue async task
    task = create_product_task.delay(
        request.niche,
        request.product_type,
        request.quality_level
    )
    
    return {
        "status": "queued",
        "task_id": task.id,
        "message": f"Creating {request.product_type} for {request.niche}"
    }


@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    """Get task status"""
    
    task = create_product_task.AsyncResult(task_id)
    
    return {
        "task_id": task_id,
        "status": task.status,
        "result": task.result if task.status == 'SUCCESS' else None
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
