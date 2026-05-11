from langchain_ollama import OllamaLLM

# 1. Model define karein (phi3 fast hai, llama3 use karna hai toh wahi likho)
# Make sure aapne 'ollama run phi3' terminal mein pehle chala liya ho
llm = OllamaLLM(model="phi3") 

def ask_ai(prompt):
    print("AI is thinking...\n")
    
    # 2. .stream() use karne se output fast dikhega
    # Pura paragraph generate hone ka wait nahi karna padega
    for chunk in llm.stream(prompt):
        print(chunk, end="", flush=True)
    print("\n")

# 3. Test 
if __name__ == "__main__":
    user_input = "Hi, I am an AI Engineer and Python Developer specializing in Generative AI, LLMs, RAG, Agentic AI, and AI-powered applications. I am currently looking for opportunities in AI Engineering, GenAI, and AI Automation.Can you suggest some job roles that would be a good fit for my skills and experience?"
    ask_ai(user_input)