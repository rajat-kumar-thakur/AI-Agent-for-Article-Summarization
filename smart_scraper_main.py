from playwright.sync_api import async_playwright

class web_scraper:
    def __init__(self):
        self.browser = None
        self.playwright = None
        self.page = None

    async def init_browser(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.page = await self.browser.new_page()


    async def scrape_content(self, url):
        if not self.page or self.page.is_closed():
            await self.init_browser()
        await self.page.goto(url, wait_until='domcontentloaded', timeout=60000)
        await self.page.wait_for_timeout(5000) 
        content = await self.page.content()
        return content
    
    async def screenshot_buffer(self):
        if not self.page or self.page.is_closed():
            return None
        return await self.page.screenshot(type='png', full_page=False)
    
    async def close_browser(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        self.playwright = None
        self.browser = None
        self.page = None
        