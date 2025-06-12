FuriaCHATBot - Setup Rápido (Python)
Este projeto é um bot para Telegram escrito em Python que utiliza várias APIs externas. Para rodar, siga os passos abaixo com atenção.

Passo 1: Clonar o repositório
No seu terminal, clone o repositório oficial do bot:

git clone https://github.com/gabriesb/FuriaCHATBot.git
cd FuriaCHATBot
Passo 2: Criar um bot filho no Telegram
Abra o Telegram e procure pelo usuário BotFather.

Envie o comando /newbot e siga as instruções para criar seu bot filho.

Ao finalizar, o BotFather vai te passar o Token do seu bot — guarde esse token, você vai usar no .env.

Passo 3: Criar o arquivo .env
Na raiz do projeto, crie um arquivo .env com o seguinte conteúdo, substituindo as chaves e tokens pelas suas:

TWITTER_API_KEY=SEU_CODIGO_TWEEPY
GIPHY_API_KEY=SUA_CHAVE_GIPHY
TELEGRAM_BOT_TOKEN=SEU_TOKEN_BOT_TELEGRAM
HUGGINGFACE_API_KEY=SUA_CHAVE_HUGGINGFACE
Passo 4: Criar e ativar ambiente virtual (opcional, mas recomendado)

python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

Passo 5: Instalar dependências manualmente
Como não há requirements.txt, instale as bibliotecas necessárias manualmente. Exemplo comum para bots Telegram com Python:

pip install python-telegram-bot requests python-dotenv
Se seu projeto usa outras bibliotecas, instale-as conforme necessário.

Passo 6: Rodar o bot
Execute o bot com:

python main.py
(Substitua main.py pelo nome do script principal, se for diferente.)

Dicas finais
Mantenha seu arquivo .env seguro, não o envie para repositórios públicos.

Para criar outras chaves (Twitter, Giphy, HuggingFace), consulte a documentação oficial de cada serviço.

Se precisar descobrir quais bibliotecas o projeto usa, verifique os imports no código-fonte.

Pronto! Seu bot está configurado para rodar. 🚀
