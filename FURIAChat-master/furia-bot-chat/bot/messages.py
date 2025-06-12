import os
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from bot.database import obter_pergunta_aleatoria
from dotenv import load_dotenv
from bot.quiz_utils import enviar_mensagem_quiz
import aiohttp
import tweepy
import random
import requests

load_dotenv()
TENOR_API_KEY = os.getenv("TENOR_API_KEY")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
client = tweepy.Client(bearer_token=bearer_token)

async def start(update: Update,context: CallbackContext) -> None:
    await update.message.reply_text("👋 Olá, fã da FURIA! Pronto para mostrar sua paixão pelo time? 🐆")

async def ajuda(update: Update,context: CallbackContext) -> None:
    await update.message.reply_text(
        "📚 Comandos disponíveis:\n\n"
        "/start - Iniciar o bot\n"
        "/ajuda - Ver os comandos disponíveis\n"
        "/noticiasfuria - Últimas notícias da FURIA\n"
        "/lineup - Ver o elenco atual\n"
        "/giffuria - Ver um GIF maneiro da FURIA\n"
        "/motivafuria - Frase motivacional da FURIA para você\n"
        "/redesfuria - Veja as redes sociais da FURIA Esports\n"
        "/quizfuria - Participe do quiz sobre a FURIA!\n"
        "/shop - Acesse a loja da FURIA\n"
        "/curiosidadefuria - Receba alguma curiosidade sobre a FURIA!"
    )

async def noticiasfuria(update: Update,context: CallbackContext) -> None:
    try:
        response = client.search_recent_tweets(query="#FURIACS", tweet_fields=["created_at", "text", "id"], max_results=10)

        if response.data:
            tweet = response.data[0]
            tweet_text = tweet.text
            tweet_date = tweet.created_at.strftime("%d/%m/%Y %H:%M:%S")
            tweet_id = tweet.id

            tweet_link = f"https://twitter.com/FURIA/status/{tweet_id}"

            await update.message.reply_text(
                f"📰 Último Tweet sobre #FURIACS:\n\n"
                f"📅 Data: {tweet_date}\n"
                f"📝 Tweet: {tweet_text}\n\n"
                f"🔗 Veja o tweet completo: {tweet_link}"
            )
        else:
            await update.message.reply_text(
                "Nenhuma notícia recente sobre a FURIA encontrada. Tente novamente mais tarde!"
            )
    except Exception as e:
        await update.message.reply_text(f"Erro ao buscar os tweets: {str(e)}")

async def lineup(update: Update,context: CallbackContext) -> None:
    await update.message.reply_text(
        "🎮 **LineUP Atual da FURIA (CS:GO)**\n\n"
        "**1. Gabriel 'FalleN' Toledo** 🇧🇷\n"
        "📍 Nascimento: Itararé, SP, Brasil\n"
        "🎯 Função: AWPer, Capitão (IGL)\n"
        "📝 Descrição: Conhecido como 'Professor', FalleN é uma lenda do CS brasileiro, bicampeão de Major em 2016. Fundador da Games Academy, é reconhecido por sua liderança e habilidade com a AWP. \n\n"
        "**2. Yuri 'yuurih' Santos** 🇧🇷\n"
        "📍 Nascimento: Brasil\n"
        "🎯 Função: Rifler\n"
        "📝 Descrição: Parte da FURIA desde 2017, yuurih é conhecido por sua consistência e agressividade. Alcançou a marca de 1000 mapas disputados com a equipe em 2023. \n\n"
        "**3. Mareks 'YEKINDAR' Gaļinskis** 🇱🇻\n"
        "📍 Nascimento: Letônia\n"
        "🎯 Função: Rifler\n"
        "📝 Descrição: Jogador letão conhecido por seu estilo de jogo agressivo. Atuou por equipes como Virtus.pro e Team Liquid antes de se juntar à FURIA como stand-in em 2025. \n\n"
        "**4. Kaike 'KSCERATO' Cerato** 🇧🇷\n"
        "📍 Nascimento: Brasil\n"
        "🎯 Função: Rifler\n"
        "📝 Descrição: Considerado um dos melhores jogadores do Brasil, KSCERATO é conhecido por sua habilidade e consistência. Homenageou seu irmão com um sticker no Major de 2021. \n\n"
        "**5. Danil 'molodoy' Golubenko** 🇷🇺\n"
        "📍 Nascimento: Rússia\n"
        "🎯 Função: AWPer\n"
        "📝 Descrição: Jovem talento russo que se destacou na AMKAL Esports antes de se juntar à FURIA em abril de 2025, trazendo uma nova dinâmica ao time. \n\n"
    )

async def giffuria(update: Update,context: CallbackContext) -> None:
    search_term = "furia esports csgo"
    limit = 10

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://tenor.googleapis.com/v2/search?q={search_term}&key={TENOR_API_KEY}&limit={limit}"
        ) as response:
            if response.status == 200:
                data = await response.json()
                results = data.get("results")
                if results:
                    gif_url = random.choice(results)["media_formats"]["gif"]["url"]
                    await update.message.reply_animation(animation=gif_url)
                else:
                    await update.message.reply_text("Nenhum GIF encontrado 😢")
            else:
                await update.message.reply_text("Erro ao buscar o GIF 😔")

async def motivafuria(update: Update,context: CallbackContext) -> None:
    frases = [
        "🔥 Se é pra ser fácil, não é FURIA.",
        "🧠 O segredo é simples: mira na cabeça, joga com o coração.",
        "🎯 Todo dia é dia de highlight.",
        "🚀 Treine até o impossível parecer rotina.",
        "👊 As balas acabam. A vontade, nunca.",
        "🐆 Enquanto uns reclamam do eco, a FURIA ecoa pela vitória.",
        "💣 Plantar a C4 é fácil. Difícil é plantar respeito.",
        "🏆 O mouse é pesado, mas o sonho é mais ainda.",
        "🔫 Trocação é diversão. Vencer é estilo de vida.",
        "💥 O impossível só existe até alguém da FURIA fazer.",
        "⚔️ Tática ganha round. Coragem ganha campeonatos.",
        "🛡️ Se a pressão for grande, responda com ainda mais força.",
        "🎮 Jogador bom treina. Jogador FURIA evolui.",
        "💥 Clutch não é sorte. É preparo e nervo de aço.",
        "🔥 Fraco não joga. Fraco assiste.",
        "🐺 Somos predadores, não presa.",
        "👟 Sem passo pra trás. Só pra avançar.",
        "🖤 Em cada derrota, nasce uma nova fera.",
        "💣 Não desarme seu sonho.",
        "🎯 Pra que desculpas, se você pode treinar?",
        "🏹 Mira firme, porque o próximo headshot pode mudar o jogo.",
        "💪 FURIA não perde — aprende.",
        "🎮 Quem treina mais, chora menos.",
        "🔥 Se a derrota te derrubar, levanta e dá o retake.",
        "💥 Ninguém nasceu clutch — mas todo guerreiro aprende.",
        "🎯 A chance não bate na porta. Você invade o bomb e cria a sua.",
        "🖤 Coração preto e amarelo: onde a FURIA vai, a torcida vai junto.",
        "🐆 Toda fera dorme. Mas quando acorda, ninguém segura.",
        "💣 Se a vida te derrubar, responde com um HS.",
        "🎮 Foco no jogo, e o resto vem na sequência."
    ]

    frase_escolhida = random.choice(frases)
    await update.message.reply_text(f"⚡ {frase_escolhida}")


async def redesfuria(update: Update,context: CallbackContext) -> None:
    redes_sociais = """
    🌐 Redes Sociais da FURIA Esports:

📸 Instagram: [furiagg](https://www.instagram.com/furia/)
🎮 Twitch: [FURIAtv](https://www.twitch.tv/furiatv)
🎥 YouTube: [FURIAgg](https://www.youtube.com/@FURIAgg)
🐦 X: [FURIA](https://x.com/FURIA)
    """

    await update.message.reply_text(redes_sociais)

async def quizfuria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem_usuario = update.message.text.strip().lower()

    if not context.user_data.get('quiz_em_andamento') or mensagem_usuario == "/quizfuria":
        pergunta_data = obter_pergunta_aleatoria()

        if pergunta_data:
            pergunta_texto = pergunta_data[1]
            alternativa_a = pergunta_data[2]
            alternativa_b = pergunta_data[3]
            alternativa_c = pergunta_data[4]

            await enviar_mensagem_quiz(update, pergunta_texto, alternativa_a, alternativa_b, alternativa_c)

            context.user_data['quiz_pergunta_id'] = pergunta_data[0]
            context.user_data['quiz_resposta_correta'] = pergunta_data[5]
            context.user_data['quiz_em_andamento'] = True
        else:
            await update.message.reply_text("❌ Desculpe, não há perguntas disponíveis no momento!")
    else:
        resposta_usuario = mensagem_usuario
        resposta_correta = context.user_data.get('quiz_resposta_correta')

        if resposta_usuario == resposta_correta.lower():
            await update.message.reply_text("✅ Parabéns! Você acertou!")
        else:
            await update.message.reply_text(f"❌ Que pena! A resposta correta era: {resposta_correta.upper()}")
            
        context.user_data.pop('quiz_pergunta_id', None)
        context.user_data.pop('quiz_resposta_correta', None)
        context.user_data.pop('quiz_em_andamento', None)

async def shop(update: Update,context: CallbackContext) -> None:
    loja_furia = "https://www.furia.gg/"

    resposta = (
        "🔥 A FURIA está com tudo! 🔥\n\n"
        "Está procurando aquele item exclusivo? 🎽👕\n"
        f"👉 [Clique aqui para acessar a loja oficial da FURIA!]({loja_furia}) 🛒🔥\n\n"
        "Mostre seu apoio e seja FURIA! 🖤🔥 #FURIA #OrgulhoFURIA"
    )

    await update.message.reply_text(resposta, parse_mode='Markdown')




API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

async def curiosidadefuria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        prompt = (
             "Quero que você me retorne uma curiosidade ou algo sobre a FURIAGG no CS2 ou CSGO."
        )

        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.9,
                "top_p": 0.95,
                "return_full_text": False
            }
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        resultado = response.json()

        curiosidade = resultado[0]["generated_text"].strip()

        await update.message.reply_text(
            f"🎯 *Curiosidade sobre a FURIA:*\n\n_{curiosidade}_",
            parse_mode="Markdown"
        )

    except Exception as e:
        print(f"Erro ao gerar curiosidade: {e}")
        await update.message.reply_text("⚠️ Deu ruim ao buscar a curiosidade. Tenta de novo mais tarde!")


