#!/usr/bin/env python
"""
Main entry point for AI Digital Product Automation System
"""

import asyncio
import logging
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main():
    """
    Main workflow execution
    """
    
    logger.info("Starting AI Digital Product Automation System")
    logger.info("="*60)
    
    try:
        # Import after logging setup
        from orchestration.workflow_engine import ProductAutomationWorkflow
        
        # Initialize workflow
        workflow = ProductAutomationWorkflow()
        
        # Example 1: Create an eBook
        logger.info("\n🎯 EXAMPLE 1: Creating eBook")
        logger.info("-" * 60)
        
        result_ebook = await workflow.execute(
            niche='Digital Marketing',
            product_type='ebook',
            quality_level='premium'
        )
        
        logger.info(f"✅ eBook created successfully!")
        logger.info(f"   Path: {result_ebook['product_path']}")
        logger.info(f"   Quality Score: {result_ebook['quality_score']}")
        logger.info(f"   Title: {result_ebook['idea'].get('title', 'Unknown')}")
        
        # Example 2: Create a Digital Asset
        logger.info("\n🎯 EXAMPLE 2: Creating Digital Asset")
        logger.info("-" * 60)
        
        result_asset = await workflow.execute(
            niche='E-commerce',
            product_type='digital_asset',
            quality_level='premium'
        )
        
        logger.info(f"✅ Digital Asset created successfully!")
        logger.info(f"   Path: {result_asset['product_path']}")
        logger.info(f"   Quality Score: {result_asset['quality_score']}")
        
        # Example 3: Create a Video Course (placeholder)
        logger.info("\n🎯 EXAMPLE 3: Creating Video Course")
        logger.info("-" * 60)
        
        result_video = await workflow.execute(
            niche='Web Development',
            product_type='video_course',
            quality_level='premium'
        )
        
        logger.info(f"✅ Video Course created successfully!")
        logger.info(f"   Path: {result_video['product_path']}")
        logger.info(f"   Quality Score: {result_video['quality_score']}")
        
        logger.info("\n" + "="*60)
        logger.info("✨ All products created successfully!")
        logger.info("="*60)
        
        # Print summary
        logger.info("\n📊 SUMMARY:")
        logger.info(f"  • eBook: {result_ebook['product_path']}")
        logger.info(f"  • Digital Asset: {result_asset['product_path']}")
        logger.info(f"  • Video Course: {result_video['product_path']}")
        logger.info("\n🚀 All files saved to ./outputs/")
        
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    # Run async main
    asyncio.run(main())
