FuriaCHATBot - Setup Rápido
Este projeto é um bot para Telegram que usa várias APIs externas. Para rodar, siga os passos abaixo com atenção.

Passo 1: Clonar o repositório
No seu terminal, clone o repositório oficial do bot:

bash
Copiar
Editar
git clone https://github.com/gabriesb/FuriaCHATBot.git
cd FuriaCHATBot
Passo 2: Criar um bot filho no Telegram
Abra o Telegram e procure pelo usuário BotFather.

Envie o comando /newbot e siga as instruções para criar seu bot filho.

Ao finalizar, o BotFather vai te passar o Token do seu bot — guarde esse token, você vai usar no .env.

Passo 3: Criar o arquivo .env
Na raiz do projeto, crie um arquivo .env com o seguinte conteúdo, substituindo as chaves e tokens pelas suas:

env
Copiar
Editar
TWITTER_API_KEY=SEU_CODIGO_TWEEPY
GIPHY_API_KEY=SUA_CHAVE_GIPHY
TELEGRAM_BOT_TOKEN=SEU_TOKEN_BOT_TELEGRAM
HUGGINGFACE_API_KEY=SUA_CHAVE_HUGGINGFACE
Passo 4: Instalar dependências
Use o gerenciador de pacotes para instalar tudo que o projeto precisa:

bash
Copiar
Editar
npm install
# ou, se usar yarn:
# yarn install
Passo 5: Rodar o bot
Finalmente, execute o bot com:

bash
Copiar
Editar
npm start
# ou
# node index.js
Se tudo estiver certo, o bot estará funcionando e respondendo no Telegram.

Dicas finais
Mantenha seu .env seguro, nunca envie ele para repositórios públicos.

Se precisar de mais informações, consulte o README original no repositório do projeto.

Para criar outras chaves (Twitter, Giphy, HuggingFace), consulte a documentação oficial de cada serviço.

Pronto! Agora é só usar e se divertir com seu bot. 🚀
