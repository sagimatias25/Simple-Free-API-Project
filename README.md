# Simple Free API Project

## Overview

A simple and efficient Python project demonstrating how to make requests to the **Joke API** (JokeAPI) and fetch random jokes from a free API.

This project showcases:
- Making HTTP requests to external APIs
- Parsing JSON responses
- Good software engineering practices with error handling
- Returning multiple values using tuples

---

## Quick Start

### Requirements

- **Python 3.7+**
- **requests** library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sagimatias25/Simple-Free-API-Project.git
   cd Simple-Free-API-Project
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Run the code:**
   ```bash
   python main.py
   ```

---

## How It Works

### `fetch_joke(url)`

Fetches a joke from the API and returns:
- **joke_text**: The joke text
- **category**: The joke category from the API

```python
from main import fetch_joke

url = 'https://v2.jokeapi.dev/joke/Any'
joke_text, category = fetch_joke(url)
print(f"Category: {category}")
print(f"Joke: {joke_text}")
```

### Example Output:

```
Category from API: Any
Why don't scientists trust atoms? Because they make up everything!

Category from API: Programming
Why do Java developers wear glasses?
Because they can't C#
```

---

## Key Features

Support for multiple joke types:
- Single: A joke in one line
- Twopart: A joke with setup and delivery

Robust Error Handling:
- Catches API errors
- Catches parsing errors
- Returns default values

Available Categories:
- `Any` - Any joke
- `Programming` - Programming jokes
- `Knock-Knock` - Knock-knock jokes
- and more...

---

## Project Structure

```
Simple-Free-API-Project/
├── main.py           # Main file with functions
├── README.md         # This file
└── .idea/            # IDE configuration
```

---

## API Reference

### JokeAPI Endpoint
```
https://v2.jokeapi.dev/joke/{category}
```

**Available Categories:**
 `Any` - Any category
 `Programming`
 `General`
 `Dark`
 and more...

---


---

## Contributing

We welcome contributions! Here's how to help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## License

This project is open for free use.

---

## Contact

**GitHub**: [@sagimatias25](https://github.com/sagimatias25)

---

## Useful Resources

- [JokeAPI Documentation](https://jokeapi.dev/)
- [Python Requests Docs](https://requests.readthedocs.io/)
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)


