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
        page = browser.new_page()
        
        for url in urls:
            try:
                print(f"Visiting {url} to reset inactivity timer...")
                page.goto(url)
                
                # Wait 5 seconds to ensure the Streamlit WebSocket connects
                page.wait_for_timeout(5000) 
                print(f"-> Successfully pinged {url}")
                
            except Exception as e:
                print(f"-> Error visiting {url}: {e}")
                
        browser.close()

if __name__ == "__main__":
    keep_awake()
