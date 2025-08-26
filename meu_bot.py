import telebot
import time
import random

# =========== ÁREA DE CONFIGURAÇÃO ===========
# AÇÃO MAIS IMPORTANTE: COLOQUE SEU TOKEN NOVO E SEGURO AQUI

TOKEN = "8110307701:AAFU6BNDkOxzuQ44D3YGJcZkYE3BSaYLCqA"
CHAT_ID = "-1003093401447" # ID DO SEU GRUPO PRINCIPAL
INTERVALO_ENTRE_POSTS_EM_MINUTOS = 60 # RITMO NORMAL: 1 POST POR HORA

# =========== ARSENAL DE POSTS (COMPLETO E ORGANIZADO COM FILE_IDs DE FOTO) ===========

posts = [
    # Post 1
    {"legenda": "A cidade dorme, mas a putaria não 🔥\n Clica aqui pra ver o que acontece na minha cama 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANMaK09XVWqfPY_A5RRQFOhyOd3eZgAAtCuMRt4HWhFzsOs7bZNglsBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 2
    {"legenda": "Pra sua insônia... 😈 Duvido você dormir depois de assistir a isso.\n Clica embaixo 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANNaK09XZ8RNU0iemlmEHfRQCm3LG0AAtGuMRt4HWhF7G9eZDPMo-IBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 3
    {"legenda": "A essa hora, só os pervertidos estão acordados. \n Isso é pra você... 😏👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANOaK09XVXcR8L6FhDtbPrjNfbgnCkAAtKuMRt4HWhFBq8arb683YABAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 4
    {"legenda": "A vizinha ouviu uns barulhos estranhos... \n Quer saber o motivo? 🤫👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANPaK0914tlQfK7UgsCops_ZpRUFuYAAtOuMRt4HWhFPqUxD1aM640BAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 5
    {"legenda": "Vazou 💣 Me filmaram sem eu saber. \n Clica rápido antes que eu apague! 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANQaK091xANjkoXGdzxk97GK8dQjeEAAtSuMRt4HWhFidckviJzGJ8BAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 6
    {"legenda": "O vídeo que o Telegram quer banir 🔞 Censura não tem vez aqui. \n Olha embaixo 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANRaK0915MbmyLI1zSjFX-Nvmx4SQ8AAtWuMRt4HWhFxt8EsKf98ZABAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 7
    {"legenda": "Seu despertador tocou? Tenho um jeito melhor de te acordar... 💦 \n Clica aqui 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANSaK0911vR0WnGJ0ch2bXeAaSlRRoAAtauMRt4HWhFrjPTXYBJ2_kBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 8
    {"legenda": "Café da manhã tá servido 😈 Mas o prato principal é outro... \n Clica no botão 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANTaK0912mavRiETh2ZmUVUbZeieTsAAteuMRt4HWhFUD6fprr7QgYBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 9
    {"legenda": "Indo pro trabalho? Assiste isso no banheiro. Ninguém precisa saber... \n😏👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANUaK0919YhjsoVMGl_QH89mULc6NEAAhKvMRv_4WhFnCS4vPUMywIBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 10
    {"legenda": "Meu chefe não pode nem sonhar que eu gravei isso na empresa \n🤫 Clica pra ver o perigo 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANVaK0914y_mG7ysgkBHP8IJv8CJ5EAAtiuMRt4HWhFJejB1hpcSuwBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 11
    {"legenda": "Reunião chata? Foge pro meu VIP que a diversão é garantida \n🔥 Olha a saída aqui embaixo 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANWaK091-NRGZzBadJzGt0GmcXwrPMAAtmuMRt4HWhFOKVqP8noXQIBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 12
    {"legenda": "A aposta era que eu não teria coragem de postar. Perderam. \n💣 Clica e confere 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANXaK0917O9rTGS3EOR_-jpO8GEbwsAAtquMRt4HWhFaOKephjVcoABAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 13
    {"legenda": "Sua pausa pro almoço ficou muito mais interessante agora... \n🔥😏👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANYaK091xd2IaK8xEKWEKNMMYhb0h4AAtuuMRt4HWhF_kTXLb7VfbMBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 14
    {"legenda": "Isso deveria ser ILEGAL de tão gostoso 🔞 \n Acesso liberado só pros mais rápidos 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANZaK092eBW-zdnNl5Zn6SSEZc1O1IAAtyuMRt4HWhF79L5kFRpdRYBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 15
    {"legenda": "Se alguém te pegar vendo isso, diz que é um documentário 🤫\n Clica no botão pra assistir 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANaaK092WdV3-kEvtSypROPjlpdZLUAAt2uMRt4HWhFlXkhMx_DUWABAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 16
    {"legenda": "Tô sozinha em casa e me deu uma ideia... 😈 \n O resultado tá no link. Clica 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANbaK092e1kOmSztDcCgNp4RTkL4CMAAt6uMRt4HWhFdDa02wy3LiEBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 17
    {"legenda": "Aquele momento da tarde que bate um tédio... \n Resolvi seu problema 💦👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANcaK092dzZdhL786hPUlW61PRjMD0AAt-uMRt4HWhFjphi3ekbyRUBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 18
    {"legenda": "Fim do expediente. Hora de relaxar e fazer umas coisas erradas... \n 🔥 Clica aqui 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANdaK092UQ3rSdYLNY_rZFiE3cYZlUAAuKuMRt4HWhF4KJAcUZii7wBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 19
    {"legenda": "Chegou em casa? Tira a roupa e vem ver o que eu preparei pra você \n 😏🔥👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANeaK092c0xbmu5nxirKkSpFfZXRo4AAuCuMRt4HWhFQz_x7ZVwLJEBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 20
    {"legenda": "Isso é um convite 😈 O resto da noite depende de você \n clique no botão aqui embaixo 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANfaK092etjDA37aq7VJ8lBvU0FTMAAAuGuMRt4HWhFj-0RSXuH2MQBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 21
    {"legenda": "Meu vídeo mais pedido. Atendendo a ordens... e eu gosto de obedecer 💦 \n Clica 👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANgaK092ZERFtCYIQkGSOelgiF2FKAAAuOuMRt4HWhFJGqOHrzQ1uUBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 22
    {"legenda": "Agora que as crianças dormiram, a brincadeira dos adultos começa 🔞 \n Clica pra entrar no quarto 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANhaK092aYjpPa2Y4CSjpaxMyG3Wa8AAuSuMRt4HWhFkHOTijCHKbYBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 23
    {"legenda": "Sem censura, sem limites, sem frescura.\n Só o puro suco do proibido 💣👇", "midia": "AgACAgEAAyEFAAS3Vq_XAANQaK091xANjkoXGdzxk97GK8dQjeEAAtSuMRt4HWhFidckviJzGJ8BAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
    # Post 24
    {"legenda": "A última chamada da noite. Vai encarar ou vai dormir sonhando? 🔥 \n A decisão tá no botão 👉", "midia": "AgACAgEAAyEFAAS3Vq_XAANSaK0911vR0WnGJ0ch2bXeAaSlRRoAAtauMRt4HWhFrjPTXYBJ2_kBAAMCAAN5AAM2BA", "texto_botao": "👉 Ver o vídeo completo", "link_botao": "https://t.me/AnaSubzinhaVIPbot"},
]


# Daqui pra baixo, o motor da máquina.
# ---------------------------------------------------------------------
bot = telebot.TeleBot(TOKEN)

print(">>> BOT DE PRODUÇÃO INICIADO. Operação 100% interna e à prova de falhas. <<<")

while True:
    try:
        post_aleatorio = random.choice(posts)
        markup = telebot.types.InlineKeyboardMarkup()
        btn = telebot.types.InlineKeyboardButton(text=post_aleatorio["texto_botao"], url=post_aleatorio["link_botao"])
        markup.add(btn)
        
        # Usando send_photo, que agora vai funcionar perfeitamente com os file_ids de foto.
        bot.send_photo(CHAT_ID, photo=post_aleatorio['midia'], caption=post_aleatorio['legenda'], reply_markup=markup)
        print(f"Post enviado: {post_aleatorio['legenda']}")
        
        print(f"Próximo post em {INTERVALO_ENTRE_POSTS_EM_MINUTOS} minutos...")
        time.sleep(INTERVALO_ENTRE_POSTS_EM_MINUTOS * 60)
        
    except Exception as e:
        print(f"Ocorreu um erro: {e}. Verificando o file_id: {post_aleatorio.get('midia', 'N/A')}")
        time.sleep(30)