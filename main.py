import requests

def fetch_joke(url):
    """Fetch a joke from the API and return the joke text and category."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        
        # Get category from API
        category = joke_data.get('category', 'Unknown')
        
        # Parse joke based on type
        if joke_data.get('type') == 'single':
            joke_text = joke_data.get('joke', '')
        elif joke_data.get('type') == 'twopart':
            joke_text = f"{joke_data.get('setup', '')}\n{joke_data.get('delivery', '')}"
        else:
            joke_text = str(joke_data)
        
        return joke_text, category
        
    except requests.exceptions.RequestException as e:
        return f"API error: {e}", "Unknown"
    except Exception as e:
        return f"Parsing error: {e}", "Unknown"

def main():
    with requests.Session() as session:
        # Any joke
        url_any = 'https://v2.jokeapi.dev/joke/Any'
        joke_text, api_category = fetch_joke(url_any)
        print(f"Category from API: {api_category}")
        print(joke_text)
        
        # Programming joke category
        category = 'Programming'
        url_category = f'https://v2.jokeapi.dev/joke/{category}'
        joke_text, api_category = fetch_joke(url_category)
        print(f"\nCategory from API: {api_category}")
        print(joke_text)

if __name__ == "__main__":
    main()
