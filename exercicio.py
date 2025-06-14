import openai

class PythonAICoder:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_code(self, prompt, max_tokens=150):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Escreva um código Python3 para: {prompt}",
            max_tokens=max_tokens,
            temperature=0.2,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()

# Exemplo de uso:pip 
# coder = PythonAICoder("SUA_OPENAI_API_KEY")
# codigo = coder.generate_code("ler um arquivo CSV e mostrar as primeiras 5 linhas")
# print(codigo)