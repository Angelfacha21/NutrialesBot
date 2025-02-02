import telebot
from telebot import types

#Conection whit the bot
TOKEN = "7695223229:AAHaPsDVYwJZ4OsfmPUE43dKG_YYiPA_TXI"

bot = telebot.TeleBot(TOKEN)

video_path = 'Assets\Prohibido.mp4'
image_path = 'Assets\pendejutria.jpg'

respuestas_usuarios = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Create bottons
    btn_y = types.InlineKeyboardButton('Si', callback_data='si')
    btn_n = types.InlineKeyboardButton('No', callback_data='no')
    
    # Add bottons markup
    markup.add(btn_y, btn_n)
    
    bot.reply_to(message, "¡Hola! Soy el Dr. Nutriales. Lamento informarte que a partir de hoy seré tu NutriCompañero en el mundo de la salud y la alimentación. Mi misión es ayudarte a estar en forma.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    chat_id = call.message.chat.id

    if chat_id not in respuestas_usuarios:
        respuestas_usuarios[chat_id] = {}
    print(f"Callback data: {call.data}")
    chat_id = call.message.chat.id

    if call.data == 'no':
        send_shit(call.message)
    
    elif call.data in ['si']:
        send_years(call.message)

    elif call.data in ['OPA', 'OPB', 'OPC']:
        if chat_id not in respuestas_usuarios:
            respuestas_usuarios[chat_id] = {}
        respuestas_usuarios[chat_id]['edad'] = call.data
        send_stature(call.message)

    elif call.data in ['MENOS_150', '150_170', 'MAYOR_170']:
        if chat_id not in respuestas_usuarios:
            respuestas_usuarios[chat_id] = {}
        respuestas_usuarios[chat_id]['estatura'] = call.data
        send_gender(call.message)

    elif call.data in ['H', 'M']:
        if chat_id not in respuestas_usuarios: 
            respuestas_usuarios[chat_id] = {}
        respuestas_usuarios[chat_id]['genero'] = call.data       
        send_intentions(call.message)

    elif call.data in ['SP', 'MP', 'BP']:
        if chat_id not in respuestas_usuarios:
            respuestas_usuarios[chat_id] = {}
        respuestas_usuarios[chat_id]['intenciones'] = call.data
        send_weight(call.message)

    elif call.data in ['Flacow', 'Chill', 'Fat', 'Gorda']:
        if chat_id not in respuestas_usuarios:
            respuestas_usuarios[chat_id] = {}
        respuestas_usuarios[chat_id]['peso'] = call.data
        procesar_respuestas(call)
        if call.data == 'Gorda':
            send_video(call.message)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """\
Oh oh, parece que algo no anda bien. Pero no te preocupes, Nutriales está aquí para resolverlo sin causarte un infarto... ¿En qué puedo echarte una pata? Una disculpa el imbecil que me programo no coloco nada acá
\
""")

def send_video(message):
    try:
        video = open(video_path, 'rb')
        bot.send_video(message.chat.id, video)
        print("Video enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el video: {e}")


def send_image(message):
    image = open(image_path, 'rb')
    bot.send_photo(message.chat.id, image, caption="⚒️⚙️Lo sentimos pero por el momento no tenemos la información suficiente para suministrarte, seguimos en desarrollo...  Utiliza el comando /help para obtener más información⚒️⚙️")

def send_shit(message):
    bot.send_message(message.chat.id, "Puedes irte a comer una bien sucia, la consulta fueron 10$")


def send_gender(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_H = types.InlineKeyboardButton('Hombre', callback_data='H')
    btn_M = types.InlineKeyboardButton('Mujer', callback_data='M')

    markup.add(btn_H, btn_M)
    
    bot.send_message(message.chat.id, "La pregunta más importante... ¿Eres Hombre o Mujer?", reply_markup=markup)

def send_years(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_18 = types.InlineKeyboardButton('18', callback_data='OPA')
    btn_19_30 = types.InlineKeyboardButton('19-30', callback_data='OPB')
    btn_31_50 = types.InlineKeyboardButton('31-50', callback_data='OPC')
    
    markup.add(btn_18, btn_19_30, btn_31_50)
    
    bot.send_message(message.chat.id, "Buenísimo, ahora necesito saber ¿cuántos años tienes?", reply_markup=markup)

def send_stature(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_menor_150 = types.InlineKeyboardButton('< 150 cm', callback_data='MENOS_150')
    btn_150_170 = types.InlineKeyboardButton('150-170 cm', callback_data='150_170')
    btn_mayor_170 = types.InlineKeyboardButton('> 170 cm', callback_data='MAYOR_170')
    
    markup.add(btn_menor_150, btn_150_170, btn_mayor_170)
    
    bot.send_message(message.chat.id, "Gracias por compartir tu edad. Ahora, ¿cuánto mides?", reply_markup=markup)

def send_weight(message):
    markup = markup = types.InlineKeyboardMarkup(row_width=4)
    
    btn_menos_60 = types.InlineKeyboardButton('< 60 Kg', callback_data='Flacow')
    btn_entre_80 = types.InlineKeyboardButton('60 - 80Kg', callback_data='Chill')
    btn_hasta_120 = types.InlineKeyboardButton('80 - 120Kg', callback_data='Fat')
    btn_mas_120 = types.InlineKeyboardButton('> 120Kg', callback_data='Gorda')

    markup.add(btn_menos_60, btn_entre_80, btn_hasta_120, btn_mas_120)
    
    bot.send_message(message.chat.id, "Disculpa que te pregunte pero... Cuanto pesas?", reply_markup=markup)


def send_intentions(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_su = types.InlineKeyboardButton('Subir de peso', callback_data='SP')
    btn_ma = types.InlineKeyboardButton('Mantener peso', callback_data='MP')
    btn_ba = types.InlineKeyboardButton('Bajar de peso', callback_data='BP')
    
    markup.add(btn_su, btn_ma, btn_ba)
    
    bot.send_message(message.chat.id, "Vamos bien, necesito saber cual es tu objetivo", reply_markup=markup)
        

def procesar_respuestas(call):
    chat_id = call.message.chat.id
    respuestas = respuestas_usuarios.get(chat_id, {})
    edad = respuestas.get('edad', '')
    estatura = respuestas.get('estatura', '')
    genero = respuestas.get('genero', '')
    intenciones = respuestas.get('intenciones', '')
    peso = respuestas.get('peso', '')

    resumen = f"Testeo!:\nEdad: {edad}\nEstatura: {estatura}\nGénero: {genero} \nIntenciones: {intenciones}\nPeso: {peso}"
    print(resumen)
    print(respuestas_usuarios)

    bot.send_message(chat_id, resumen)

    if genero == 'H' and edad == 'OPA' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno:
Batido de proteínas con leche entera, plátano y avena (50 g).
Dos huevos revueltos.
Almuerzo:
Hamburguesa de carne magra (150 g) en pan integral.
Papas al horno (150 g).
Cena:
Filete de salmón (150 g) con arroz integral (100 g).
Ensalada mixta.
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")
    
    elif genero == 'H' and edad == 'OPA' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno:
Yogur natural (150 g) con una cucharada de miel y fresas (100 g).
Tostada integral con aguacate.
Almuerzo:
Ensalada de atún (100 g) con lechuga, tomate y pepino.
Quinoa (50 g) cocida.
Cena:
Pechuga de pollo a la plancha (120 g) con verduras al vapor.
Una manzana como postre.
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion y caminatas ligeras.
""")

    elif genero == 'H' and edad == 'OPA' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Avena cocida (40 g) con agua y canela.
Un té sin azúcar.
Almuerzo:
Pechuga de pavo (120 g) con espárragos al vapor.
Ensalada de espinacas.
Cena:
Pescado blanco al horno (120 g) con brócoli.
Una naranja como postre.
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")

    elif genero == 'H' and edad == 'OPB' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno:
Tostadas integrales con mantequilla de maní y plátano.
Almuerzo:
Pasta integral (100 g) con salsa boloñesa (carne magra).
Cena:
Pizza casera con abundantes vegetales y queso.
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")

    elif genero == 'H' and edad == 'OPB' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno:
Smoothie de frutas con yogur natural.
Almuerzo:
Pollo asado (100 g) con ensalada verde.
Cena:
Tortilla española con verduras.
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion y caminatas ligeras.
""")

    elif genero == 'H' and edad == 'OPB' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno:
Yogur griego bajo en grasa con semillas.
Almuerzo:
Ensalada grande con garbanzos y aderezo ligero.
Cena:
Sopa de verduras y una pechuga pequeña a la plancha.
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")
    
    elif genero == 'H' and edad == 'OPC' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno:
Avena cocida con leche descremada y frutas.
Almuerzo:
Filete de pollo a la plancha con puré de patatas.
Cena:
Verduras asadas y una porción pequeña de quinoa.
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion y caminatas ligeras.
""")
    
    elif genero == 'H' and edad == 'OPC' and intenciones == 'MP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'H' and edad == 'OPC' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno:
Smoothie verde (espinacas, plátano, agua).
Almuerzo:
Ensalada César ligera sin crutones y pollo a la parrilla.
Cena:
Pescado al vapor con espárragos y limón.
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")
    
    elif genero == 'M' and edad == 'OPA' and intenciones == 'SP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPA' and intenciones == 'MP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPA' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno:
Batido energético con leche, avena, plátano y mantequilla de almendra.
Almuerzo:
Lentejas guisadas (150 g) con arroz integral.
Cena:
Salteado de tofu y verduras sobre arroz basmati
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")

    elif genero == 'M' and edad == 'OPB' and intenciones == 'SP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPB' and intenciones == 'MP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPB' and intenciones == 'BP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPC' and intenciones == 'SP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPC' and intenciones == 'MP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    elif genero == 'M' and edad == 'OPC' and intenciones == 'BP':
        bot.send_message(chat_id, f"Continue")
        send_image(call.message)

    else:
        bot.send_message(chat_id, f"Disculpa pero no suministraste toda la información que necesito :(, intentalo de nuevo con /start")

bot.polling()
