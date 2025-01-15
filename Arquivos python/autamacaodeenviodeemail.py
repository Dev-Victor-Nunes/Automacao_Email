import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#dados conexão
username = "227932024@eniac.edu.br"
senha = "pokemonfirered3301"

#informações do email para enviar
dest = "227932024@eniac.edu.br"
assunto = "teste de envio"
corpo = "Bazinga! Geronimooooo!"

#configurar a mensagem
mensagem = MIMEMultipart()
mensagem['From'] = username
mensagem['To'] = dest
mensagem['Subject'] = assunto
mensagem.attach( MIMEText(corpo,'plain') )

try:
  with smtplib.SMTP('smtp.gmail.com', 587) as server :
    server.starttls()
    server.login(username, senha)
    server.sendmail(username, dest, mensagem.as_string() )
  print("E-mail enviado com sucesso")
except Exception as e :-
  print("Erro ao enviar o email")