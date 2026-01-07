from playwright.sync_api import sync_playwright
import os

username = "Jarmil"
password = "Admin123"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://souhrada.github.io/playwright-exam/")

        page.fill('#login', username)
        page.fill('#pass', password)

        page.click('.login-btn')

        secret_message = page.locator('.super-secret-text').text_content()

        print(secret_message)

        browser.close()
    

if __name__ == "__main__":
    main()
