# TranslateHUB

## Sobre

É uma API  de tradução que permite traduzir texto de uma língua para outra. A API é rápida e fácil de usar, com suporte a mais de 100 línguas.

## Como usar

Instale as seguintes dependências:

- `deep_translator`
- `Flask`

Use:

`pip install deep_translator` e `pip install flask`

### Métodos da API

- `/v1/translate` - Traduz o texto enviado para outra língua.
- `/v1/languages` - Lista todas as línguas suportadas.

### Como usar os métodos

#### Traduzir texto usando `/v1/translate`

```bash
curl -X POST http://127.0.0.1:5000/v1/translate \
-H "Content-Type: application/json" \
-d '{
    "text": "Hello, world!",
    "origin": "en",
    "target": "es"
}'

```

#### Listar texto usando `/v1/languages`

```bash
curl -X GET http://127.0.0.1:5000/v1/languages
```
