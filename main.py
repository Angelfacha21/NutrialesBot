import telebot
from telebot import types

#Conection whit the bot
TOKEN = "7695223229:AAHaPsDVYwJZ4OsfmPUE43dKG_YYiPA_TXI"

bot = telebot.TeleBot(TOKEN)

video_path = "Assets/Prohibido.mp4"
image_path = "Assets/pendejutria.jpg"

respuestas_usuarios = {}

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    # Create bottons
    btn_y = types.InlineKeyboardButton('Dietas 🍽️', callback_data='si')
    btn_n = types.InlineKeyboardButton('NO 😡', callback_data='no') 
    btn_a = types.InlineKeyboardButton('Alergias ⚒️', callback_data='a') 
    btn_ay = types.InlineKeyboardButton('Ayuda 🫂', callback_data='ay') 
    btn_i = types.InlineKeyboardButton('❗INFORMACIÓN❗', callback_data='i') 
    
    # Add bottons markup
    markup.add(btn_y, btn_a, btn_ay, btn_n, btn_i)
    
    bot.reply_to(message, "¡Hola, hola! ¡Soy el Dr. Nutriales, tu nuevo compañero en esta emocionante aventura de salud y alimentación! Prepárate para descubrir juntos los secretos de una vida más sana y divertida. ¡No te preocupes, no te voy a aburrir con charlas complicadas ni dietas imposibles! Mi misión es hacerte sentir genial, ¡así que vamos a ponerle sabor y alegría a tu bienestar! \n ¿Necesitas ayudas en... ?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    chat_id = call.message.chat.id

    if chat_id not in respuestas_usuarios:
        respuestas_usuarios[chat_id] = {}
    print(f"Callback data: {call.data}")
    chat_id = call.message.chat.id
    
    if call.data == 'i':
        send_info(call.message)

    elif call.data == 'a':
        send_image(call.message)

    elif call.data == 'ay':
        send_help(call.message)

    elif call.data == 'no':
        send_shit(call.message)

    elif call.data == 'si':
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
    bot.reply_to(message, f"""\
¡Ups! Parece que las cosas se pusieron un poco raras por aquí. ¡Pero no te preocupes, Nutriales está al rescate! Sin pánico, estoy aquí para ayudarte a resolver cualquier problema sin que te dé un ataque al corazón. \n
¿Qué te trae por aquí? ¡Cuéntame tus problemas con confianza! Cualquier cosa reclamale al "tarado" ese que me programó, ¡todos tenemos nuestros días! Lo importante es que estoy aquí para echarte una mano (o una pata, como prefieras). \n
Cualquier sugerencia o problema que estes teniendo hazmela saber en: docnutriales@gmail.com \
""")

@bot.message_handler(commands=['restart'])
def send_restart(message):
    bot.send_message(message.chat.id, f"""¿Qué ha sucedido? No nos queda de otra... He we go again""")
    send_welcome(message)

def send_video(message):
    try:
        video = open(video_path, 'rb')
        bot.send_video(message.chat.id, video)
        print("Video enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el video: {e}")


def send_info(message):
    bot.send_message(message.chat.id, f"""⚠️ AVISO LEGAL ⚠️ \n
Este bot, Nutriales, ha sido creado con fines educativos y de entretenimiento. La información suministrada a través de este servicio no debe ser interpretada como asesoramiento médico, nutricional o de salud profesional. Aunque hacemos esfuerzos para asegurar que la información proporcionada sea precisa y actualizada, no garantizamos su exactitud ni completitud. \n

LIMITACIÓN DE RESPONSABILIDAD \n
No nos hacemos responsables por cualquier acción tomada basada en la información proporcionada por Nutriales. El uso de esta información es bajo su propio riesgo. \n

DERECHOS DE AUTOR ©️ \n
Todo el contenido y material proporcionado por Nutriales está protegido por derechos de autor y no puede ser reproducido, distribuido o utilizado sin el permiso expreso del autor. \n

MODIFICAIONES Y TERMINACIÓN \n
Nos reservamos el derecho de modificar, suspender o terminar el acceso a este bot en cualquier momento y por cualquier motivo, sin previo aviso.
""")

def send_image(message):
    image = open(image_path, 'rb')
    bot.send_photo(message.chat.id, image, caption="⚒️⚙️ ¡Vaya, parece que me pillaste en medio de una actualización! ¡Pero no te preocupes, la información que necesitas está en camino! \n Mientras tanto, puedes usar el comando /help para descubrir los secretos que ya conozco. ¡Te prometo que la espera valdrá la pena!⚒️⚙️")

def send_shit(message):
    bot.send_message("""message.chat.id,Pensé que querías mi ayuda, ¡me ha dolido en mi nutricorazón esta traición! Pero no te preocupes, ya me he comido un snack para curar mis penas y estoy listo para volver a la acción. ¡Volvamos a empezar, sin dramas esta vez!""")

#def send_aler(message):
#    image = open(image_path, 'rb')
#    bot.send_photo(message.chat.id, image, caption="¡Oh, me atrapaste en plena sesión de programación! 💻 Pero no te preocupes, la información que necesitas está en camino, solo falta un poco más de magia codificadora. Mientras tanto, prueba el comando /help para explorar los misterios que ya tengo listos. ¡Te aseguro que la espera valdrá cada byte!")

def send_gender(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    btn_H = types.InlineKeyboardButton('Hombre', callback_data='H')
    btn_M = types.InlineKeyboardButton('Mujer', callback_data='M')

    markup.add(btn_H, btn_M)
    
    bot.send_message(message.chat.id, "¡Ajá! ¡La pregunta del millón! ¿Eres hombre o mujer? ¡O tal vez algo intermedio! ¡O quizás eres un ser de otro planeta que no encaja en ninguna de estas categorías! ¡No te preocupes, no te juzgaré! ¡Solo necesito saberlo para poder personalizar tu experiencia NutriCompañero!", reply_markup=markup)

def send_years(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_18 = types.InlineKeyboardButton('18', callback_data='OPA')
    btn_19_30 = types.InlineKeyboardButton('19-30', callback_data='OPB')
    btn_31_50 = types.InlineKeyboardButton('31-50', callback_data='OPC')
    
    markup.add(btn_18, btn_19_30, btn_31_50)
    
    bot.send_message(message.chat.id, "¡Genial! Ahora, ¿cuántos años tienes? ¡Solo necesito saberlo para ayudarte a estar en forma!", reply_markup=markup)

def send_stature(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_menor_150 = types.InlineKeyboardButton('< 150 cm', callback_data='MENOS_150')
    btn_150_170 = types.InlineKeyboardButton('150-170 cm', callback_data='150_170')
    btn_mayor_170 = types.InlineKeyboardButton('> 170 cm', callback_data='MAYOR_170')
    
    markup.add(btn_menor_150, btn_150_170, btn_mayor_170)
    
    bot.send_message(message.chat.id, "Necesito saber tu estatura para ajustar nuestros planes de salud. ¿Eres un gigante que toca el techo o alguien que se esconde en las multitudes? ", reply_markup=markup)

def send_weight(message):
    markup = markup = types.InlineKeyboardMarkup(row_width=4)
    
    btn_menos_60 = types.InlineKeyboardButton('< 60 Kg', callback_data='Flacow')
    btn_entre_80 = types.InlineKeyboardButton('60 - 80Kg', callback_data='Chill')
    btn_hasta_120 = types.InlineKeyboardButton('80 - 120Kg', callback_data='Fat')
    btn_mas_120 = types.InlineKeyboardButton('> 120Kg', callback_data='Gorda')

    markup.add(btn_menos_60, btn_entre_80, btn_hasta_120, btn_mas_120)
    
    bot.send_message(message.chat.id, "¡Es hora de hablar de números! ¿Cuánto marca la báscula? ¡No te preocupes, todos tenemos nuestro peso ideal! ¡Lo importante es estar saludables y felices!", reply_markup=markup)


def send_intentions(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    
    btn_su = types.InlineKeyboardButton('Subir de peso', callback_data='SP')
    btn_ma = types.InlineKeyboardButton('Mantener peso', callback_data='MP')
    btn_ba = types.InlineKeyboardButton('Bajar de peso', callback_data='BP')
    
    markup.add(btn_su, btn_ma, btn_ba)
    
    bot.send_message(message.chat.id, "¿Quieres perder peso? ¿Ganar masa muscular? ¿Simplemente comer más sano y sentirte con más energía? ¡Cuéntame tus sueños y metas!", reply_markup=markup)

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

    #bot.send_message(chat_id, resumen)

    if genero == 'H' and edad == 'OPA' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno:
Desayuno: Tostadas integrales con aguacate y huevo revuelto. \n
Almuerzo: Hamburguesa de pavo con pan integral, lechuga, tomate y batatas al horno. \n
Cena: Arroz integral con salmón a la parrilla y brócoli al vapor. \n
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
Recuerda que son recomendaciones, mejorare las dietas y rutina en cuestión de tiempo
""")
    
    elif genero == 'H' and edad == 'OPA' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno: Yogur griego con granola y fruta fresca. \n
Almuerzo: Wrap integral de pollo a la parrilla con espinacas. \n
Cena: Pasta integral con salsa pesto y tomates cherry. \n
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion moderada y caminatas ligeras.
""")

    elif genero == 'H' and edad == 'OPA' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno: Batido verde (espinacas, plátano y agua). \n
Almuerzo: Wrap integral de pavo con verduras frescas. \n
Cena: Pescado al horno con quinoa y espinacas salteadas. \n
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")

    elif genero == 'H' and edad == 'OPB' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno: Tortilla de tres huevos con espinacas y queso feta. \n
Almuerzo: Ensalada César con pollo a la parrilla y pan crujiente. \n
Cena: Pizza casera con masa integral, verduras y pepperoni. \n
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")

    elif genero == 'H' and edad == 'OPB' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno: Tortilla española (huevo y patata). \n
Almuerzo: Ensalada mediterránea (tomate, pepino, feta). \n
Cena: Filete a la parrilla acompañado por puré de patatas. \n
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion moderada y caminatas ligeras
""")

    elif genero == 'H' and edad == 'OPB' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno: Omelette de claras de huevo con champiñones. \n
Almuerzo: Ensalada de garbanzos con pepino y tomate. \n
Cena: Pechuga de pavo al horno con espárragos asados. \n
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")
    
    elif genero == 'H' and edad == 'OPC' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno: Avena cocida con nueces y plátano. \n
Almuerzo: Ensalada de atún con garbanzos y aderezo de yogur. \n
Cena: Pollo al horno con arroz basmati y espárragos. \n
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")
    
    elif genero == 'H' and edad == 'OPC' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno: Smoothie proteico (plátano y espinacas). \n
Almuerzo: Hamburguesa magra en pan integral sin mayonesa. \n
Cena: Pollo asado acompañado por verduras al vapor. \n
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion moderada y caminatas ligeras.
""")

    elif genero == 'H' and edad == 'OPC' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno: Avena cocida solo en agua o leche baja en grasa. \n
Almuerzo: Ensalada mixta sin aderezo o aderezo ligero. \n
Cena: Pollo al grill acompañado por verduras asadas. \n
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")

    elif genero == 'M' and edad == 'OPA' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno: Batido de plátano con leche entera, avena y mantequilla de maní. \n
Almuerzo: Ensalada de pollo con quinoa, aguacate y aderezo de aceite de oliva. \n
Cena: Pasta integral con salsa de tomate, carne molida magra y queso parmesano. \n
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
Recuerda que son recomendaciones, mejorare las dietas y rutina en cuestión de tiempo
""")

    elif genero == 'M' and edad == 'OPA' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno: Tostadas integrales con aguacate y huevo poché. \n
Almuerzo: Quinoa con verduras asadas y garbanzos. \n
Cena: Salteado de pollo con arroz integral y brócoli. \n
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion moderada y caminatas ligeras.
""")

    elif genero == 'M' and edad == 'OPA' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno: Avena cocida con frutas frescas y canela. \n
Almuerzo: Ensalada mixta con atún, lechuga, tomate y vinagreta. \n
Cena: Pechuga de pollo a la plancha con verduras al vapor. \n
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta 
""")

    elif genero == 'M' and edad == 'OPB' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno: Yogur griego con granola, frutos secos y miel. \n
Almuerzo: Wrap de pollo con espinacas, hummus y pimientos asados. \n
Cena: Tacos de carne asada con frijoles negros y guacamole. \n
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")

    elif genero == 'M' and edad == 'OPB' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno: Avena cocida con frutas secas. \n
Almuerzo: Pollo a la parrilla sobre una cama de espinacas frescas. \n
Cena: Pescado al horno acompañado por quinoa. \n
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion moderada y caminatas ligeras.
""")

    elif genero == 'M' and edad == 'OPB' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno: Yogur natural con frutos rojos. \n
Almuerzo: Sopa de verduras casera. \n
Cena: Tofu salteado con brócoli y arroz integral. \n
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")

    elif genero == 'M' and edad == 'OPC' and intenciones == 'SP':
        bot.send_message(chat_id, f"""Desayuno: Smoothie de frutas con yogur griego y avena. \n
Almuerzo: Sopa de lentejas con pan integral. \n
Cena: Filete de ternera con puré de patatas y judías verdes. \n
Para aumentar de peso, especialmente en forma de masa muscular, es crucial enfocarse en ejercicios de resistencia. Como las sentadillas, levantamiento de pesa, flexiones y dominadas.
""")

    elif genero == 'M' and edad == 'OPC' and intenciones == 'MP':
        bot.send_message(chat_id, f"""Desayuno: Batido de proteínas con frutas. \n
Almuerzo: Sopa minestrone rica en vegetales. \n
Cena: Salteado de tofu con verduras mixtas. \n
Se recomienda una actividad física moderada para no perder peso, algunos ejercicios que pueden servir pueden ser natacion moderada y caminatas ligeras.
""")

    elif genero == 'M' and edad == 'OPC' and intenciones == 'BP':
        bot.send_message(chat_id, f"""Desayuno: Smoothie de bayas sin azúcar añadido. \n
Almuerzo: Ensalada César ligera (sin aderezo cremoso). \n
Cena: Filete de pescado a la parrilla con espinacas al vapor. \n
Para perder peso, se deben priorizar los ejercicios que aumentan el gasto calórico. Algunas opciones eficaces son: correr o andar en bicicleta
""")

    else:
        bot.send_message(chat_id, f"Disculpa pero no suministraste toda la información que necesito :(, intentalo de nuevo con /restart")

bot.polling()
