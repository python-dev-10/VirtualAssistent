import speech_recognition as sr

import smtplib
from email.message import EmailMessage

receiver = ''
subject = ''
senderEmail = 'stinghenvsk@gmail.com'
senderPassword = 'Stinghen2021'

def para(frase):
  try:
    global receiver
    receiver = frase.split('para ')[1]
    print(receiver)

  except Exception as e:
    print(e)
    return 'Assistente: Não foi possivel enviar o email'
  
  return 'Assistente: Qual vai ser o assunto do e-mail?'

def assunto(frase):
  try:
    global subject
    subject = frase.split('assunto é ')[1]
    print(subject)

  except Exception as e:
    print(e)
    return 'Assistente: Não foi possivel enviar o email'

  return 'Assistente: Qual vai ser o conteúdo do e-mail?'

def conteudo(frase):
  try:
    message = frase.split('conteúdo é ')[1]
    print(message)

  except Exception as e:
    print(e)
    return 'Assistente: Não foi possivel enviar o email'

  msg = EmailMessage()
  msg['Subject'] = subject
  msg['From'] = senderEmail
  print(receiver)
  msg['To'] = receiver
  msg.set_content(message)

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(senderEmail, senderPassword)
    smtp.send_message(msg)

  return 'Assistente: Email enviado!'