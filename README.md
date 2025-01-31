# Let Me Cook 🍳

An AI-powered recipe generation application that creates personalized recipes based on your available ingredients.

## Features ✨

- **Ingredient-Based Recipe Generation**: Input your available ingredients and get customized recipes
- **Multi-Language Support**: Generate recipes in English, Telugu, Hindi, and Tamil
- **Real-Time Generation**: Watch engaging loading animations with fun cooking quotes while your recipe is being created
- **Detailed Recipes**: Get complete recipes with:
  - Recipe title
  - Description
  - Ingredient list with quantities
  - Step-by-step cooking instructions
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Technology Stack 🛠️

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

5. Open your browser and navigate to:
```
http://localhost:5000
```

## How to Use 📝

1. Enter available ingredients one by one with their quantities
2. Click "ADD" after each ingredient
3. Once finished adding ingredients, click "Let's Cook"
4. Optionally add a description and select preferred language
5. Submit and wait for your personalized recipe
6. View your generated recipe with complete instructions

## Project Structure 📁

```
LetMeCook/
├── static/
│   ├── styles.css
│   └── dev_pic.png
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── recipe.html
│   └── contact.html
├── app.py
├── model_res.py
└── requirements.txt
```

## Contributing 🤝

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature requests.

## Contact 📧

- **Developer**: Pranay Akhil Jeedimalla
- **Email**: jpranayakhil066@gmail.com
- **LinkedIn**: [Pranay Akhil Jeedimalla](https://www.linkedin.com/in/pranay-akhil-jeedimalla-578676252/)
- **GitHub**: [akhilbrucelee066](https://github.com/akhilbrucelee066)

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Google Generative AI for providing the AI model
- Flask community for the excellent web framework
- All contributors and users of the application