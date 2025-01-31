import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
import json

api_key = 'AIzaSyCV7s5lxc7HcUkNbeb37cpDumiiuBLUeB8'

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 0.8,
  "top_p": 0.85,
  "top_k": 40,
  "max_output_tokens": 6192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    required = ["validResponse", "recipeTitle", "description", "ingredients", "instructions"],
    properties = {
      "validResponse": content.Schema(
        type = content.Type.BOOLEAN,
      ),
      "recipeTitle": content.Schema(
        type = content.Type.STRING,
      ),
      "description": content.Schema(
        type = content.Type.STRING,
        description = "A brief description of the recipe in 50 words"
      ),
      "ingredients": content.Schema(
        type = content.Type.STRING,
      ),
      "instructions": content.Schema(
        type = content.Type.OBJECT,
        properties = {
          "0": content.Schema(type = content.Type.STRING),
          "1": content.Schema(type = content.Type.STRING),
          "2": content.Schema(type = content.Type.STRING),
          "3": content.Schema(type = content.Type.STRING),
          "4": content.Schema(type = content.Type.STRING),
          "5": content.Schema(type = content.Type.STRING),
          "6": content.Schema(type = content.Type.STRING),
          "7": content.Schema(type = content.Type.STRING),
          "8": content.Schema(type = content.Type.STRING),
          "9": content.Schema(type = content.Type.STRING),
          "10": content.Schema(type = content.Type.STRING),
          "11": content.Schema(type = content.Type.STRING),
        }
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="You are a world-class chef and expert in recipe generation. Based on the user's input of available ingredients and a brief description, generate the best possible cooking recipe. You may include basic supporting ingredients like salt, water, sugar, or oil only if necessary for the recipe. user input:",
)

chat_session = model.start_chat()



def generate_recipe(user_input):
    try:
        ingredients = user_input['ingredients']
        preferences = user_input.get('preferences', {})
        
        prompt = f"Ingredients: {', '.join(ingredients)}\n"
        if preferences.get('description'):
            prompt += f"Additional context: {preferences['description']}\n"
        if preferences.get('language'):
            prompt += f"Preferred language: {preferences['language']}\n"
        
        recipe_data = chat_session.send_message(prompt)
        recipe_json = json.loads(recipe_data.text)
        return recipe_json
    except Exception as e:
        return {
            "validResponse": False,
            "recipeTitle": "Error",
            "description": f"Failed to generate recipe: {str(e)}",
            "ingredients": "Error occurred while processing ingredients",
            "instructions": {}
        }