import requests

def fetch_joke(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        
        # Basic joke parsing
        if joke_data.get('type') == 'single':
                        return joke_data.get('joke', ''), joke_data.get('category', 'Unknown')
            return f\"{joke_data.get('setup', '')}\n{joke_data.get('delivery', '')}\", joke_data.get('category', 'Unknown')
                    return str(joke_data), joke_data.get('category', 'Unknown')
    except requests.exceptions.RequestException as e:
        return f"API error: {e}"
    except Exception as e:
        return f"Parsing error: {e}"

def main():
    with requests.Session() as session:
        # Any joke
        url_any = 'https://v2.jokeapi.dev/joke/Any'
        joke_text, api_category = fetch_joke(url_any)
                print(f"Category from API: {api_category}")
        
        # Programming joke category
        category = 'Programming'
        url_category = f'https://v2.jokeapi.dev/joke/{category}'
        joke_text, api_category = fetch_joke(url_category)
        print(f"\nCategory from API: {api_category}\n{joke_text}")

if __name__ == "__main__":
    main()

