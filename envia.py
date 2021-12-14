from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'aqui vai seu email'
minha_senha = 'aqui vai sua senha'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Eduardo Cezar', data=data_atual) #aqui você vai alterar as tags do template

msg = MIMEMultipart()
msg['from'] = 'SEU NOME'
msg['to'] = 'email do cliente'  # Cliente
msg['subject'] = 'ASSUNTO DO E-MAIL'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
