from django.shortcuts import render
import openai
import os

api_key = os.environ.get('OPENAI_API_KEY')


def generate_response(request):
    response_to_user = None
    recipe_to_user = None

    if api_key is not None and request.method == "POST":
        openai.api_key = api_key

        user_input = request.POST.get('user_input')

        prompt = f"Я маю наступні продукти:{user_input}. Що я можу з цього приготувати?"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=256)
        print(response)

        response_to_user = response["choices"][0]["text"]

        prompt = f"Можеш сказати рецепт{response} цього?"

        reciper = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=256)
        print(response)

        recipe_to_user = reciper["choices"][0]["text"]

    return render(request, 'ai_response.html', {'response': response_to_user, 'recipe': recipe_to_user})
