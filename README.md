# Job-Search-Agent
Job Automation done using AI agent

Here is the full project explanation, with code flow.

Project Purpose

This is a job automation bot. Its job is:

Search jobs from LinkedIn.
1. Pick top job links.
2. Send those jobs to local AI model phi3 through Ollama.
3. AI gives match score based on your skills.
4. Email the final job analysis to you.

Main flow starts from job_agent.py (line 56).

Files

job_agent.py 

This is the main controller/orchestrator. It connects scraper, AI, and mailer.

scraper.py 

This opens LinkedIn using Playwright and collects job title, company, and link.

main.py 

This connects your project with local Ollama AI model phi3.

mailer.py 

This sends the AI-generated job analysis to email using Gmail SMTP.

run_bot.bat 

This is a Windows shortcut script to activate the environment and run the bot.
