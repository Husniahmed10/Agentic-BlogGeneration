from langchain_openai import ChatOpenAI 
import os 
from dotenv import load_dotenv 

class OpenLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            self.openai_api_key=os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
            llm = ChatOpenAI(api_key=self.openai_api_key, model="gpt-4o")
            return llm 
        
        except Exception as e:
            raise ValueError("Error occured with exception : {e}")