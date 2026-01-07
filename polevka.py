from bs4 import BeautifulSoup
import requests
import json


def main():
    data = {}
    url = "https://souhrada.github.io/bsoup-exam/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # BeautifulSoup(response.content, "html.parser") <--- Úkol: popiš krátce, co tohle dělá
    # čte přesně html, aby věděl co má číst
    
    # ingredients = soup.locator('.stuff').first.inner_text()
    # print(ingredients)

    ingredients = soup.select('.stuff')

    # for i in ingredients:
    #     print(i) # mohlo by se hodit in range()
    
    print(ingredients.get_text())

    data["ingredients:"] = ingredients

    with open("recept.json", "w") as file:
        json.dump(data, file, indent=4)



if __name__ == "__main__":
    main()