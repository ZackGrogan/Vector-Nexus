import os
import logging
import numpy as np
from typing import List, Optional
import aiohttp
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class EmbeddingsGenerator:
    def __init__(self):
        """Initialize the embeddings generator with API configurations."""
        self.huggingface_api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        self.huggingface_api_url = os.getenv('HUGGINGFACE_API_URL', 
            'https://api-inference.huggingface.co/models/sentence-transformers/all-mpnet-base-v2')
        
        # Initialize Gemini
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if gemini_api_key:
            genai.configure(api_key=gemini_api_key)
        
        self.session = None

    async def get_session(self) -> aiohttp.ClientSession:
        """Get or create an aiohttp session."""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    def normalize_embedding(self, embedding: List[float]) -> List[float]:
        """
        Normalize the embedding vector to unit length.
        
        Args:
            embedding: The embedding vector to normalize
            
        Returns:
            List[float]: The normalized embedding vector
        """
        embedding_array = np.array(embedding)
        norm = np.linalg.norm(embedding_array)
        if norm > 0:
            normalized = embedding_array / norm
            return normalized.tolist()
        return embedding

    async def generate_embeddings_huggingface(self, text: str) -> Optional[List[float]]:
        """
        Generate embeddings using Hugging Face's API.
        
        Args:
            text: The text to generate embeddings for
            
        Returns:
            Optional[List[float]]: The embedding vector if successful, None if failed
        """
        if not self.huggingface_api_token:
            logger.error("Hugging Face API token not configured")
            return None

        try:
            session = await self.get_session()
            headers = {"Authorization": f"Bearer {self.huggingface_api_token}"}
            
            async with session.post(
                self.huggingface_api_url,
                headers=headers,
                json={"inputs": text}
            ) as response:
                if response.status != 200:
                    logger.error(f"Hugging Face API error: {response.status}")
                    return None
                    
                result = await response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0]
                    
                logger.error(f"Unexpected response format from Hugging Face: {result}")
                return None

        except Exception as e:
            logger.error(f"Error generating embeddings with Hugging Face: {e}")
            return None

    async def generate_embeddings_gemini(self, text: str) -> Optional[List[float]]:
        """
        Generate embeddings using Google's Gemini API.
        
        Args:
            text: The text to generate embeddings for
            
        Returns:
            Optional[List[float]]: The embedding vector if successful, None if failed
        """
        try:
            model = genai.GenerativeModel('embedding-001')
            result = model.embed_content(text)
            
            if hasattr(result, 'embedding'):
                return result.embedding
                
            logger.error("No embedding in Gemini response")
            return None

        except Exception as e:
            logger.error(f"Error generating embeddings with Gemini: {e}")
            return None

    async def fallback_embedding(self, text: str) -> Optional[List[float]]:
        """
        Try to generate embeddings using Hugging Face first, then fall back to Gemini.
        
        Args:
            text: The text to generate embeddings for
            
        Returns:
            Optional[List[float]]: The embedding vector if successful with either service, None if both fail
        """
        # Try Hugging Face first
        embedding = await self.generate_embeddings_huggingface(text)
        if embedding:
            logger.info("Successfully generated embeddings with Hugging Face")
            return embedding

        # Fall back to Gemini
        logger.info("Falling back to Gemini for embeddings generation")
        embedding = await self.generate_embeddings_gemini(text)
        if embedding:
            logger.info("Successfully generated embeddings with Gemini")
            return embedding

        logger.error("Failed to generate embeddings with both services")
        return None

    async def close(self):
        """Close the aiohttp session."""
        if self.session and not self.session.closed:
            await self.session.close()
