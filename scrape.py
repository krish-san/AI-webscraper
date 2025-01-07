from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection

SBR_WEBDRIVER = 'https://brd-customer-hl_347b7f41-zone-ai_scraper-country-us:x8zf0zaorkut@brd.superproxy.io:9515'


def scrape_web(website):
    print("launching browser...")
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        # CAPTCHA handling
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_body(html_content):
    soup=BeautifulSoup(html_content,"html.parser")
    body_content=soup.body
    if body_content:
        return str(body_content)
    return ""
def clean_body(body_content):
    soup=BeautifulSoup(body_content,"html.parser")
    for script_nd_style in soup(["script","style"]):
        script_nd_style.extract()

    cleaned_content=soup.get_text(separator="\n")
    cleaned_content="\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content 

def split_dom_content(dom_content, maxlen=6000):
    return [
        dom_content[i: i + maxlen] for i in range(0,len(dom_content),maxlen)
    ]
