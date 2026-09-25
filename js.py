import asyncio
from crawailer import Browser


async def fetch_one(browser, website_url, js_query):
    result = await browser.fetch_page(
        website_url,
        script_before=js_query
    )

    return result.get("script_result")


async def fetch_many(website_urls, js_queries):
    async with Browser() as browser:

        tasks = [
            fetch_one(browser, website_url, js_query)
            for website_url, js_query in zip(website_urls, js_queries)
        ]

        results = await asyncio.gather(*tasks)

        return results


async def main(website_urls, js_queries):
    results = await fetch_many(website_urls, js_queries)
    return results


if __name__ == "__main__":
    website_urls = ["https://example.com"]
    js_queries = [
        "document.querySelector('h1')?.textContent"
    ] 
    results = asyncio.run(main(website_urls, js_queries))
    print(results)
