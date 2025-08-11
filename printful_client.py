import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()
PRINTFUL_API_URL = "https://api.printful.com/v2/"
PRINTFUL_HEADERS = {
    "Authorization": f"Bearer {os.getenv('PRINTFUL_API_KEY')}"
}

def upload_to_printful(image_data):
    """Uploads binary image data to Printful's file library."""
    try:
        upload_url = f"{PRINTFUL_API_URL}files"
        headers_with_content = PRINTFUL_HEADERS.copy()
        files = {
            'file': ('image.png', image_data, 'image/png')
        }

        response = requests.post(upload_url, headers=headers_with_content, files=files)
        response.raise_for_status()
        return response.json()['result']['files'][0]['id']
    except requests.exceptions.RequestException as e:
        raise Exception(f"Printful file upload failed: {e}")

def create_hoodie_mockup(file_id):
    """Creates a hoodie mockup with the uploaded file."""
    try:
        mockup_url = f"{PRINTFUL_API_URL}mockup-generator/create-task"
        data = {
            "variant_ids": [6320], # Men's Hoodie
            "format": "jpg",
            "files": [
                {
                    "placement": "front",
                    "file_id": file_id
                }
            ]
        }
        headers_with_json = PRINTFUL_HEADERS.copy()
        headers_with_json["Content-Type"] = "application/json"
        
        response = requests.post(mockup_url, headers=headers_with_json, json=data)
        response.raise_for_status()
        task_id = response.json()['result']['task_key']
        
        while True:
            task_status_url = f"{PRINTFUL_API_URL}mockup-generator/tasks/{task_id}"
            status_response = requests.get(task_status_url, headers=headers_with_json)
            status_response.raise_for_status()
            status_data = status_response.json()['result']

            if status_data['status'] == 'completed':
                return status_data['mockups'][0]['extra']['preview_url']
            
            time.sleep(3)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Printful mockup creation failed: {e}")