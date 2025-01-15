pip install imap_tools

from imap_tools import MailBox, A

#dados para conexão
userName = "227932024@eniac.edu.br"
senha = "pokemonfirered3301"

meu_email = MailBox("imap.gmail.com").login(userName, senha, 'INBOX')

lista_emails = meu_email.fetch(A (subject= "teste"))

for email in lista_emails :
  print(email.from_)
  print(email.subject)
  print(email.text)