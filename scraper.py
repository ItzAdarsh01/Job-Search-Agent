from playwright.sync_api import sync_playwright
import urllib.parse

def get_job_links(role, location):
    # LinkedIn ka direct search URL (Bypassing Google)
    encoded_role = urllib.parse.quote(role)
    encoded_loc = urllib.parse.quote(location)
    
    # Ye URL direct jobs dikhata hai bina login/google ke
    url = f"https://www.linkedin.com/jobs/search?keywords={encoded_role}&location=India&f_TPR=r604800" # f_TPR=r86400 matlab last 1 week ki jobs
    
    jobs = []
    with sync_playwright() as p:
        # Headless=True rakhein taaki server par bina browser window khule chale
        browser = p.chromium.launch(headless=True) 
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36")
        page = context.new_page()
        
        print(f"Direct LinkedIn search shuru kar raha hu: {role} in {location}...")
        
        try:
            page.goto(url, wait_until="networkidle")
            
            # LinkedIn ke job cards ko dhoondhna
            job_cards = page.locator('div.base-search-card__info').all()
            
            for card in job_cards[:5]: # Sirf top 5 jobs
                title = card.locator('h3.base-search-card__title').inner_text().strip()
                company = card.locator('h4.base-search-card__subtitle').inner_text().strip()
                # Link nikalne ke liye parent element par jana hoga
                link = page.locator(f'a:has-text("{title}")').first.get_attribute('href')
                
                jobs.append({
                    "title": f"{title} at {company}",
                    "link": link.split('?')[0] if link else "No Link"
                })
            
            browser.close()
            return jobs
        except Exception as e:
            print(f"Error: {e}")
            browser.close()
            return []