from flask import Flask, jsonify, request, json
from deep_translator import GoogleTranslator, exceptions
import time

app = Flask(__name__)

def translate_text(text, target, source='auto'):
    translator = GoogleTranslator(source=source, target=target)
    default_status = "error"
    total = None

    if text: 
        try:
            begin = time.time()
            translation = translator.translate(text)
            end = time.time()
            total = round(end - begin, 2)  # Corrigido aqui
            default_status = "success"  # Corrigido aqui
        except exceptions.TranslationNotFound as NFT_EXCEPT:
            translation = "Translation not found"
        except Exception as E:
            translation = str(E)  # Corrigido aqui

        return translation, total, default_status

@app.route('/v1/translate', methods=['POST'])
def translate():
    data = request.json

    text = data['text'] # Obrigatório
    origin = data['origin'] # Obrigatório
    target = data['target'] # Obrigatório

    translation, total, status = translate_text(
        text=text,
        source=origin,
        target=target
    )
        
    return jsonify({
        "data": {
            "original-text": text,
            "translated-text": translation,
            "source-language": origin,
            "target-language": target,
            "time-to-translate": total,
            "status": status
        }
    }), 200
    
@app.route('/v1/languages', methods=['GET'])
def list_lang():
    langs = GoogleTranslator().get_supported_languages()
    template = {"supported_languages": langs}
    
    return jsonify(template)

if __name__ == '__main__':
    
    app.run()