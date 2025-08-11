# ai-hoodie-generator

# I have made this application using flassk , openai api, i have also created a form (index.html) to check the response , while my openai api is saying to add a payment method to continue , so may be this error can #occur sometime , as open ai api's are billed, i tried 4-5 accounts but all account api is returning the same output.


This project is a simple web application that uses AI to automatically generate a custom hoodie design, title, and description based on a user's prompt. It is built to demonstrate proper API integration, clear project structure.

## How to Run the Project

1.  Clone the Repository:
    ```bash
    git clone [https://github.com/divyans3799/ai-hoodie-generator.git](https://github.com/divyans3799/ai-hoodie-generator.git)
    cd ai-hoodie-generator
    ```

2.  Create a Virtual Environment and Install Dependencies:
    ```bash
    python -m venv venv
    # For Windows:
    venv\Scripts\activate
    # For macOS/Linux:
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  Set Up Environment Variables:
    Create a `.env` file in the root directory. Copy the structure from the `.env.example` file and replace the placeholder values with your actual API keys.
    ```env
    OPENAI_API_KEY="your_openai_api_key"
    PRINTFUL_API_KEY="your_printful_api_key"
    ```

4.  Run the Flask Server:
    ```bash
    python app.py
    ```

5.  Access the Application:
    Open your browser and navigate to `http://127.0.0.1:5000`.

