import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import json

from openai_client import generate_image_with_openai, generate_product_description_with_openai
from printful_client import upload_to_printful, create_hoodie_mockup

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page for the web interface."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_hoodie():
    """Main endpoint to orchestrate the generation process."""
    try:
        data = request.json
        prompt = data.get("prompt")
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        image_data = generate_image_with_openai(prompt)

        product_title, product_description = generate_product_description_with_openai(prompt)

        # Upload image to Printful
        file_id = upload_to_printful(image_data)

        printful_mockup_url = create_hoodie_mockup(file_id)

        # output
        output = {
            "printful_mockup_url": printful_mockup_url,
            "product_title": product_title,
            "product_description": product_description
        }
        
        return jsonify(output)

    except Exception as e:
        app.logger.error(f"An error occurred during generation: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
