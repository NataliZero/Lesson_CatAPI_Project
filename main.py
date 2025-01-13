import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]['url']
        else:
            return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
