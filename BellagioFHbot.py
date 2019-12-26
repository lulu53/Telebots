import telebot
import re
import datetime

bot = telebot.TeleBot("970464340:AAEauncqFI34Yz7eyf-Zhz8q4PeY7ICOFQ8")

buyers = ["io", "pb", "lex", "vb", "nr"]

#Добавление платежа в файл
def addBill(name, sumbill):
	file = open('billlog.txt','r')
	textFile = file.read()
	file.close()
	
	#r'\b' + buyers[temp] + r'\b';

	today = datetime.datetime.now()
	today = today.strftime("%Y.%m.%d_%H.%M")
	newBillStr = name + " - " + str(today) + ":" + sumbill + " "

	i = name + " - "
	textBefore = textFile.replace(i, newBillStr)
	print(textBefore)

	file = open('billlog.txt','w')
	file.write(textBefore)
	file.close()

	#textBefore = re.findall(reg_exp,textFile)


	#reg_exp = r + name + '\s-\s[^;]+'
	#re.findall(reg_exp,textFile)

	#file = open('billlog.txt','w')
	


def handle_messages(messages):
	for message in messages:
		#bot.reply_to(message, message.text) 

	#получаем сообщение и переводи в нижний регистр
		intext = message.text
		intext = intext.lower()

		#перебираем
		
		if re.search(r'\bотправил\b', intext):
			temp = 0
			#проходимся по всем баерам пока не найдем совпадения
			while temp < len(buyers):

				#регулярка для поиска баера в сообщении
				reg_exp = r'\b' + buyers[temp] + r'\b';
				#print(reg_exp + " " + intext + "\n")

				#Если баер найдее
				if re.search(reg_exp, intext):

					#Определить сумму
					print(intext)

					sumresult = re.findall(r'\d+', intext)
					print(sumresult)

					sumres = str(sumresult[0])
					
					addBill(buyers[temp], sumres)

					#finance [temp] += sumbill
					#answer = "Отправлено +" + buyers[temp] + str(sumbill)
					

					#регулярка чтобы достать строку со всеми пополнениями по баеру
					#reg_exp = r'buyers[temp]\s-\s[^;]+'

					answer = "Зачислено " + buyers[temp] + " " + sumres + "!"
					break
				else: 
					answer = "Не введен получатель"
				temp += 1
		else:
			answer = "Не задана команда (Отправить)"
		
	
	bot.send_message(message.chat.id, answer)

bot.set_update_listener(handle_messages)

bot.polling( none_stop = True )