import ollama
from flask import Flask, request, jsonify

# Inicializace Flask aplikace
app = Flask(__name__)

@app.route('/')
def index():
    return 'API je aktivní'

@app.route('/ask', methods=['POST'])
def ask_ai():
    # Získání dotazu od uživatele z frontendu
    user_query = request.json.get('query')

    if user_query:
        try:
            # Zavolání Ollama API pro získání odpovědi
            response = ollama.chat(model="llama2", messages=[{"role": "user", "content": user_query}])
            
            # Získání odpovědi z response
            answer = response['text']
            
            # Odeslání odpovědi zpět klientovi
            return jsonify({"response": answer})

        except Exception as e:
            return jsonify({"error": str(e)})

    return jsonify({"error": "No query provided!"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)  # Spuštění Flask aplikace
