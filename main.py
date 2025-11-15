import requests

def fetch_joke(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        
        # Basic joke parsing
        if joke_data.get('type') == 'single':
            return joke_data.get('joke', '')
        elif joke_data.get('type') == 'twopart':
            return f"{joke_data.get('setup', '')} {joke_data.get('delivery', '')}"
        return str(joke_data)
    except requests.exceptions.RequestException as e:
        return f"API error: {e}"
    except Exception as e:
        return f"Parsing error: {e}"

def main():
    with requests.Session() as session:
        # Any joke
        url_any = 'https://v2.jokeapi.dev/joke/Any'
        print(fetch_joke(url_any))
        
        # Programming joke category
        category = 'Programming'
        url_category = f'https://v2.jokeapi.dev/joke/{category}'
        joke_text = fetch_joke(url_category)
        print(f"\nCategory: {category}\n{joke_text}")

if __name__ == "__main__":
    main()
