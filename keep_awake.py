from playwright.sync_api import sync_playwright

def keep_awake():
    urls = [
        "https://econdev-bdj33mjik9zmk2qkd2z9zx.streamlit.app/",
        "https://ev-grid-simulator-fzccxa2iughvvvakpuubgs.streamlit.app/",
        "https://nationalgridsimulator-niahbu7tmj2eaycjtu6tpu.streamlit.app/",
        "https://nfl-success-map-6jraysbtpjlwzniacjks39.streamlit.app/"
    ]
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Add a real User-Agent to bypass basic bot blocking
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        for i, url in enumerate(urls):
            try:
                print(f"Visiting {url}...")
                page.goto(url, wait_until="domcontentloaded")
                
                # Wait up to 30 seconds for the Streamlit app to actually render
                page.wait_for_selector('[data-testid="stAppViewContainer"]', timeout=30000)
                
                # Give the WebSocket 3 extra seconds to register the active connection
                page.wait_for_timeout(3000)
                
                print(f"-> Successfully pinged and rendered {url}")
                
            except Exception as e:
                print(f"-> Error visiting {url}: {e}")
            finally:
                # Capture a screenshot regardless of success or failure
                screenshot_name = f"app_{i}_status.png"
                page.screenshot(path=screenshot_name)
                print(f"-> Saved screenshot as {screenshot_name}")
                
        browser.close()

if __name__ == "__main__":
    keep_awake()
