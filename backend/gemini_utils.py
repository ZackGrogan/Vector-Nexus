import os
import logging
import google.generativeai as genai
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Configure Gemini
gemini_api_key = os.getenv('GEMINI_API_KEY')
if gemini_api_key:
    genai.configure(api_key=gemini_api_key)

async def clean_text_with_gemini(text: str) -> Optional[str]:
    """
    Use Gemini to clean and validate text content.
    
    Args:
        text: The text content to clean
        
    Returns:
        Optional[str]: The cleaned text if successful, None if failed
    """
    try:
        # Configure the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Create the prompt
        prompt = f"""
        Clean and validate the following text content. Remove any inappropriate content, 
        fix formatting issues, and ensure it's well-structured. Return only the cleaned text.
        If the content is inappropriate or invalid, return 'INVALID'.

        TEXT TO CLEAN:
        {text}
        """
        
        # Generate response
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            logger.error("Empty response from Gemini")
            return None
            
        cleaned_text = response.text.strip()
        
        # Check if content was marked as invalid
        if cleaned_text == 'INVALID':
            logger.warning("Content marked as invalid by Gemini")
            return None
            
        return cleaned_text

    except Exception as e:
        logger.error(f"Error cleaning text with Gemini: {e}")
        return None
