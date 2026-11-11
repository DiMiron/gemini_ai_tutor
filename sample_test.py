
from google import genai
from google.genai import errors
from google.genai import types
import os

client = genai.Client(
    api_key="AIzaSyCGRsqcXAo9J8SkVTmHp_h6PduzDjYbkMk"
)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Поясни концепцію асинхронності в Python у 3 реченнях."
    )

    print("Відповідь Gemini:")
    print(response.text)

    response_one = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Вода яка (синоніми)"
    )

    print("Відповідь Gemini 1:")
    print(response_one.text)

except errors.ClientError as e:
    if e.code == 429:
        print("Перевищено ліміт Gemini API.")
        print("Спробуй пізніше або перевір квоту.")
    else:
        print(f"Помилка API: {e}")
