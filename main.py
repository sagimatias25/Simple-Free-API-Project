import requests

# Define the endpoint URL for a random joke
url = 'https://v2.jokeapi.dev/joke/Any'

try:
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()

        if joke_data.get('type') == 'single':
            joke_text = joke_data.get('joke', '')
        elif joke_data.get('type') == 'twopart':
            joke_text = f"{joke_data.get('setup', '')} {joke_data.get('delivery', '')}"
        else:
            joke_text = str(joke_data)

        # Print the joke text
        print(joke_text)

        category = 'Programming'
        category_url = f'https://v2.jokeapi.dev/joke/{category}'

        category_response = requests.get(category_url)

        if category_response.status_code == 200:
            category_joke_data = category_response.json()

            category_name = category_joke_data.get('category', category)

            if category_joke_data.get('type') == 'single':
                category_joke_text = category_joke_data.get('joke', '')
            elif category_joke_data.get('type') == 'twopart':
                category_joke_text = f"{category_joke_data.get('setup', '')} {category_joke_data.get('delivery', '')}"
            else:
                category_joke_text = str(category_joke_data)

            print(f"\nCategory: {category_name}")
            print(category_joke_text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
