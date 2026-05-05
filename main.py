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

# 3. Test karein
if __name__ == "__main__":
    user_input = "Hii, I am a full stack developer in php, laravel, react.js. help me find the jobs?"
    ask_ai(user_input)