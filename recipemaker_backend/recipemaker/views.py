from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.generativeai as genai

GEMINI_API_KEY='YOUR_GEMINI_API_KEY'
@api_view(['POST'])
def get_recipe_recommendations(request):
    # Get the list of ingredients and cuisine type from the request

    ingredients = request.data.get('ingredients', [])
    cuisine_type = request.data.get('cuisine_type', '')
    print(ingredients,cuisine_type)
    genai.configure(api_key=GEMINI_API_KEY)
    # Call the Gemini API to get recipe recommendations
    model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction='You are a helpful assistant that provides recipe recommendations based on ingredients and cuisine type.')
    chat = model.start_chat()
    response = chat.send_message(f"Can you suggest some recipes using {', '.join(ingredients)} from {cuisine_type} cuisine?")
    
    # Process the response from the Gemini API
    response_text = response.text

    # Return the recipe recommendations
    print(response_text)
    return Response({'text': response_text})
