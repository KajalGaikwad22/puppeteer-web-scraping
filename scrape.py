import asyncio
import json
import os
from pyppeteer import launch

async def scrape_data():
    browser = await launch(headless=False)  # Change to True for headless mode
    page = await browser.newPage()

    # Emulate human-like behavior
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    )

    try:
        await page.goto('https://abrahamjuliot.github.io/creepjs/')

        # Add delay to simulate human behavior
        await asyncio.sleep(2)

        # Scraping data with error checks
        trust_score_elem = await page.querySelector('#trust')
        lies_elem = await page.querySelector('#lies')
        bot_elem = await page.querySelector('#bot')
        fp_id_elem = await page.querySelector('#fpid')

        if trust_score_elem and lies_elem and bot_elem and fp_id_elem:
            trust_score = await page.evaluate('(element) => element.textContent.trim()', trust_score_elem)
            lies = await page.evaluate('(element) => element.textContent.trim()', lies_elem)
            bot = await page.evaluate('(element) => element.textContent.trim()', bot_elem)
            fp_id = await page.evaluate('(element) => element.textContent.trim()', fp_id_elem)

            # Save data to JSON
            data = {
                'trustScore': trust_score,
                'lies': lies,
                'bot': bot,
                'fpId': fp_id,
            }

            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=2)

            # Create PDF
            await page.pdf({'path': 'page.pdf', 'format': 'A4'})

    except Exception as e:
        print(f'Error: {e}')
    finally:
        await browser.close()

async def main():
    # Run the scraping function three times
    for _ in range(3):
        await scrape_data()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
