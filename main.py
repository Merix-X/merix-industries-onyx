import ollama
from flask import Flask, request, jsonify

# Inicializace Flask aplikace
app = Flask(__name__)

@app.route('/')
def index():
    return 'API je aktivní'

@app.route('/ask', methods=['POST'])
def ask_ai():
    user_query = request.json.get('query')
    if user_query:
        try:
            # Debugování - Ujistíme se, že dotaz přišel
            print(f"Received query: {user_query}")

            # Zavolání Ollama API
            response = ollama.chat(model="llama2", messages=[{"role": "user", "content": user_query}])

            # Debugování - Zobrazení odpovědi
            print(f"Ollama response: {response}")

            # Získání odpovědi z response
            answer = response['text']
            
            # Odeslání odpovědi zpět klientovi
            return jsonify({"response": answer})

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return jsonify({"error": str(e)})

    return jsonify({"error": "No query provided!"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
