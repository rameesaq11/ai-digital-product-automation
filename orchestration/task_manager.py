"""
Celery Task Manager - Async task execution
"""

from celery import Celery
import os

app = Celery('product_automation')

# Configuration
app.conf.broker_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
app.conf.result_backend = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
app.conf.task_serializer = 'json'
app.conf.accept_content = ['json']
app.conf.result_serializer = 'json'
app.conf.timezone = 'UTC'
app.conf.enable_utc = True


@app.task
def create_product_task(niche, product_type, quality_level='premium'):
    """Async product creation task"""
    from orchestration.workflow_engine import ProductAutomationWorkflow
    import asyncio
    
    workflow = ProductAutomationWorkflow()
    result = asyncio.run(workflow.execute(niche, product_type, quality_level))
    
    return result
