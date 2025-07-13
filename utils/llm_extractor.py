import os
import json

from openai import OpenAI
from dotenv import load_dotenv
from schemas.article_schema import EuronArticleList

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def process_llm(html, instructions, truncate=False):
    if not html:
        return None

    max_len = 15000
    content_to_send = html[:max_len] if truncate and len(html) > max_len else html

    try:
        completion = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are an expert web scraping agent. Your task is to extract:
1. title
2. articleUrl (absolute URL)
3. imageUrl
4. excerpt
from this page's HTML.

Instructions: {instructions}

Return ONLY a JSON object matching the expected schema."""
                },
                {
                    "role": "user",
                    "content": content_to_send
                }
            ],
            temperature=0.1,
            response_format="json"
        )

        response = completion.choices[0].message.content
        return EuronArticleList.model_validate_json(response)

    except Exception as e:
        print(f"Error processing LLM: {e}")
        return None
