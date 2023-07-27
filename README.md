# BybitGPTX

BybitGPTX est un bot de trading qui utilise l'IA pour prendre des décisions de trading. Il utilise l'API OpenAI pour générer des actions de trading en fonction des données du marché.

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/0xRichy/BybitGPTX.git
```

2. Accédez au répertoire du projet :
```bash
cd BybitGPTX
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Avant de pouvoir utiliser le bot, vous devez définir vos clés API pour OpenAI et Bybit. Vous pouvez le faire en définissant les variables suivantes dans le fichier `BybitGPT.py` :

```python
OPENAI_API_KEY = 'votre_clé_api_openai'
BYBIT_API_KEY = 'votre_clé_api_bybit'
BYBIT_API_SECRET = 'votre_secret_api_bybit'
```

Remplacez `'votre_clé_api_openai'`, `'votre_clé_api_bybit'` et `'votre_secret_api_bybit'` par vos véritables clés API.

Une fois que vous avez défini vos clés API, vous pouvez exécuter le bot avec la commande suivante :

```bash
python scripts/BybitGPT.py
```

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
```
