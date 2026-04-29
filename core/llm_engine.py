"""
Ollama LLM Engine - Local LLM inference
"""

import logging
import requests
import json
from typing import Optional, List, Dict

logger = logging.getLogger(__name__)


class OllamaLLMEngine:
    """Interface for Ollama LLM models"""
    
    def __init__(self, host: str = "http://localhost:11434"):
        self.host = host
        self.api_url = f"{host}/api"
        self.verify_connection()
    
    def verify_connection(self) -> bool:
        """Verify connection to Ollama server"""
        try:
            response = requests.get(f"{self.api_url}/tags", timeout=5)
            if response.status_code == 200:
                logger.info("✅ Connected to Ollama server")
                return True
            else:
                logger.error(f"Failed to connect to Ollama: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"Cannot connect to Ollama at {self.host}: {str(e)}")
            logger.info("Make sure Ollama is running: docker-compose up -d ollama")
            return False
    
    def generate(
        self,
        model: str,
        prompt: str,
        temperature: float = 0.7,
        top_p: float = 0.95,
        num_predict: int = 2000,
    ) -> str:
        """Generate text using Ollama"""
        
        try:
            payload = {
                "model": model,
                "prompt": prompt,
                "temperature": temperature,
                "top_p": top_p,
                "num_predict": num_predict,
                "stream": False,
            }
            
            response = requests.post(
                f"{self.api_url}/generate",
                json=payload,
                timeout=300
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', '')
            else:
                logger.error(f"Error from Ollama: {response.status_code}")
                return ""
        
        except Exception as e:
            logger.error(f"Error generating text: {str(e)}")
            return ""
    
    def embed(
        self,
        model: str,
        text: str,
    ) -> List[float]:
        """Generate embeddings using Ollama"""
        
        try:
            payload = {
                "model": model,
                "prompt": text,
            }
            
            response = requests.post(
                f"{self.api_url}/embeddings",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('embedding', [])
            else:
                logger.error(f"Error generating embeddings: {response.status_code}")
                return []
        
        except Exception as e:
            logger.error(f"Error during embedding: {str(e)}")
            return []


class IdeaGenerator:
    """Generate product ideas using LLM"""
    
    def __init__(self, llm: OllamaLLMEngine):
        self.llm = llm
    
    def generate_ideas(self, niche: str, trends: List[str], count: int = 5) -> List[Dict]:
        """Generate product ideas"""
        
        trends_str = ", ".join(trends[:5]) if trends else "general market trends"
        
        prompt = f"""
Generate {count} unique, high-value digital product ideas in the '{niche}' niche.

Current trends: {trends_str}

For each idea, provide:
- Title
- Problem it solves
- Target audience
- Market demand (1-10)
- Why it would work

Focus on IDEAS THAT ARE UNDERSERVED but have HIGH DEMAND.

Format each idea clearly separated by ---
"""
        
        response = self.llm.generate(
            model='mistral',
            prompt=prompt,
            temperature=0.7,
        )
        
        ideas = self._parse_ideas(response, count)
        logger.info(f"Generated {len(ideas)} ideas")
        
        return ideas
    
    def _parse_ideas(self, text: str, count: int) -> List[Dict]:
        """Parse generated ideas"""
        
        ideas = []
        
        # Simple parsing - split by --- and extract title
        sections = text.split('---')
        
        for i, section in enumerate(sections[:count]):
            if section.strip():
                lines = section.strip().split('\n')
                title = lines[0] if lines else f"Idea {i+1}"
                
                ideas.append({
                    'title': title.replace('Title:', '').strip(),
                    'content': section.strip(),
                    'market_demand': 7 + (i % 3),  # Default scoring
                    'problem_solved': f'Market opportunity in niche segment {i+1}',
                    'target_audience': 'Digital product consumers',
                })
        
        return ideas[:count]


class ContentWriter:
    """Write high-quality content using LLM"""
    
    def __init__(self, llm: OllamaLLMEngine):
        self.llm = llm
    
    def write_section(
        self,
        topic: str,
        subtopics: List[str],
        depth: str = 'comprehensive',
        word_count: int = 1500,
    ) -> str:
        """Write a section of content"""
        
        subtopics_str = "\n".join([f"- {s}" for s in subtopics]) if subtopics else "- Key concepts\n- Implementation"
        
        if depth == 'comprehensive':
            prompt = f"""
Write a COMPREHENSIVE, DETAILED section about: {topic}

Include these subtopics:
{subtopics_str}

Requirements:
- Include real-world examples
- Add case studies where relevant
- Provide actionable insights
- Use clear, professional language
- Include statistics/data
- Add expert perspectives
- Target word count: {word_count}
- Use clear headers for organization

Write as an expert would for a premium product.
"""
        else:
            prompt = f"""
Write a professional section about: {topic}

Cover these topics:
{subtopics_str}

Requirements:
- Clear and concise
- Professional tone
- Practical examples
- Target word count: {word_count}
- Well-organized
"""
        
        response = self.llm.generate(
            model='mistral',
            prompt=prompt,
            temperature=0.6,
            num_predict=word_count + 500,
        )
        
        logger.info(f"Generated content for: {topic}")
        return response
