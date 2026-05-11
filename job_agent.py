import scraper
import mailer
from main import ask_ai, llm 

def start_hunting():
    # User Preferences
    my_skills = "Python, Generative AI, LLMs, RAG, Agentic AI, AI Agents, LangChain, LangGraph, Prompt Engineering, Vector Databases, AI Automation, MCP, Ollama, FastAPI, Machine Learning, NLP, REST APIs, PHP, Laravel, MySQL, JavaScript, React.js"
    # role_to_search = "AI Engineer | Generative AI Engineer | Python Developer | Laravel Developer | LLMs & RAG"
    role_to_search = "Generative AI Engineer"
    location = "India"

    print(f"--- Starting Hunt for {role_to_search} in {location} ---")

    # 1. Fetch data from scraper
    found_jobs = scraper.get_job_links(role_to_search, location)

    # 2. Agar abhi bhi nahi mili, toh 'React' keyword se try karein (Secondary fallback)
    if not found_jobs:
        print("Initial search failed, trying alternative skill search...")
        found_jobs = scraper.get_job_links("AI/ML Engineer", location)

    if not found_jobs:
        print("No jobs found even with broad search. Check LinkedIn URL manually.")
        return

    # 2. Format job data for AI
    job_data = "\n".join([f"JOB: {j['title']} | URL: {j['link']}" for j in found_jobs[:5]])
    
    # 3. Highly Strict Prompt
    final_prompt = f"""
    [STRICT DATA PARSING MODE]
    INPUT SKILLS: {my_skills}
    JOB DATA:
    {job_data}

    CONSTRAINTS:
    - OUTPUT FORMAT: [Job Title] | [Link] | Match: X/10
    - NO introduction, NO greeting, NO advice.
    - If a job doesn't match skills, still list it with a low score.
    - Plain text only.
    """

    # ouptut
    # ask_ai(final_prompt)

    print("Analyzing jobs with AI and generating email...")
    
    # 4. Invoke AI (Mailing ke liye full string chahiye, isliye invoke use karein)
    full_analysis = llm.invoke(final_prompt)
    
    # 5. Output display and Send Email
    print("\n--- FINAL RESULTS ---")
    print(full_analysis)
    
    mailer.send_job_email(full_analysis)

if __name__ == "__main__":
    start_hunting()