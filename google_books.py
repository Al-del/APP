import requests
import json

def search_books(keyword):
    # Define the endpoint URL
    url = f"https://www.googleapis.com/books/v1/volumes?q={keyword}"

    # Send a GET request to the Google Books API
    response = requests.get(url)

    # If the request was successful, print the titles of the books
    if response.status_code == 200:
        data = response.json()
        for book in data['items']:
            print(book['volumeInfo']['title'])
    else:
        print(f"Request failed with status code {response.status_code}")

# Call the function with a keyword to search for
search_books("Quantum")