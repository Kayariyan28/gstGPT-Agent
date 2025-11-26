import google.generativeai as genai
from app.core.config import settings
from app.services.agent_tools import agent_tools
from app.core.context import last_tool_output

class LLMService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        if self.api_key != "mock-key":
            genai.configure(api_key=self.api_key)
            
            # Define tools available to the model
            self.tools = [
                agent_tools.get_sales_summary,
                agent_tools.get_tax_liability,
                agent_tools.draft_gstr1,
                agent_tools.check_compliance_status
            ]
            
            self.model = genai.GenerativeModel(
                'gemini-flash-latest',
                tools=self.tools
            )

    def generate_answer(self, query: str, context: list) -> dict:
        if self.api_key == "mock-key":
            return {
                "answer": f"**[MOCK GEMINI RESPONSE]**\n\n(Set GEMINI_API_KEY to use real model)\n\nBased on context:\n\n" + "\n".join([c.get('text', '')[:100] + "..." for c in context]),
                "tool_context": None
            }

        context_str = "\n\n".join([c.get('text', '') for c in context])
        
        # Reset context var
        last_tool_output.set(None)
        
        # System instruction with context
        system_prompt = f"""You are an expert GST Counsel and Agent for India.
        
        You have access to the following Knowledge Base about GST Laws:
        {context_str}
        
        You also have access to TOOLS to query the user's data (Sales, Tax Liability) and perform actions (Draft Returns).
        
        Rules:
        1. If the user asks a general question about GST (e.g. "What is the rate?"), use the Knowledge Base.
        2. If the user asks about THEIR data (e.g. "What is my sales?"), use the TOOLS.
        3. If the user asks to perform an action (e.g. "Draft GSTR-1"), use the TOOLS.
        4. Always be helpful and professional.
        """

        try:
            # Start a chat session to handle function calling loop automatically (mostly)
            chat = self.model.start_chat(enable_automatic_function_calling=True)
            
            # Send the system prompt + user query
            response = chat.send_message(f"{system_prompt}\n\nUser Question: {query}")
            
            # Retrieve tool output from context var
            tool_context = last_tool_output.get()

            return {
                "answer": response.text,
                "tool_context": tool_context
            }
        except Exception as e:
            return {
                "answer": f"Error generating response: {str(e)}",
                "tool_context": None
            }

llm_service = LLMService()
