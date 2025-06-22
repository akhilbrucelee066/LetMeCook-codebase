# Let Me Cook

An AI-powered recipe generation application that creates personalized recipes based on your available ingredients.

- **Ingredient-Based Recipe Generation**: Input your available ingredients and get customized recipes
- **Multi-Language Support**: Generate recipes in English, Telugu, Hindi, and Tamil
- **Real-Time Generation**: Watch engaging loading animations with fun cooking quotes while your recipe is being created
- **Detailed Recipes**: Get complete recipes with:
  - Recipe title
  - Description
  - Ingredient list with quantities
  - Step-by-step cooking instructions
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Technology Stack:

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **AI Model**: Google's Gemini AI
- **API**: Google GenerativeAI API

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Set up your Google API key:
   - Get an API key from Google AI Studio
   - Replace the API key in `model_res.py`

3. Run the application:
```bash
python app.py
```
