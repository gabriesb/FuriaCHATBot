async def enviar_mensagem_quiz(update, pergunta, alternativa_a, alternativa_b, alternativa_c):
    mensagem = f"🎮 **Vamos lá, guerreiro!** 🔥\n\n" \
               f"🚨 **Pergunta da vez:** {pergunta}\n\n" \
               f"a) {alternativa_a} 😎\n" \
               f"b) {alternativa_b} 🤔\n" \
               f"c) {alternativa_c} 💡\n\n" \
               f"Escolha a alternativa correta e mande a **letra** da sua resposta (a, b ou c)! 🏆💥"

    await update.message.reply_text(mensagem)