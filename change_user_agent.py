from selenium import webdriver
import time
from fake_useragent import UserAgent

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
user_agent = UserAgent()
user_agent_list = [
    # Sony Xperia XZ
    """Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) 
    Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36""",
    # HTC Desire 21 Pro 5G
    """Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) 
    Chrome/85.0.4183.127 Mobile Safari/537.36""",
    # Apple iPhone 6
    """Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko)
    Version/3.0 Mobile/1A543 Safari/419.3"""
]

options = webdriver.ChromeOptions()
# Random user agent
# options.add_argument(f"user-agent={user_agent.random}")
for i in user_agent_list:
    options.add_argument(f"user-agent={i}")
    browser = webdriver.Chrome(options=options)

    try:
        browser.get(url=url)
        browser.get_screenshot_as_png()
        time.sleep(5)
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()
