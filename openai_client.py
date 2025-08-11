import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()

# Initialize the OpenAIAPI key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_image_with_openai(prompt):
    
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        
        return image_response.content
    except Exception as e:
        raise Exception(f"OpenAI image generation failed: {e}")

def generate_product_description_with_openai(title):
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a creative product copywriter. Generate a compelling product title and a detailed product description for a hoodie."},
                {"role": "user", "content": f"Create a title and description for a hoodie featuring the design of a '{title}'. The output should be a JSON object with 'title' and 'description' keys."}
            ],
            response_format={ "type": "json_object" }
        )
        
        response_json = response.choices[0].message.content
        data = json.loads(response_json)

        return data.get("title"), data.get("description")
    except Exception as e:
        raise Exception(f"OpenAI text generation failed: {e}")
