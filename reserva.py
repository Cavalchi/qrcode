# Importar as bibliotecas necessárias
import qrcode
import datetime
import geocoder
from PIL import Image, ImageDraw, ImageFont

# Obter a hora e o local atuais
hora = datetime.datetime.now()
local = geocoder.ip('me').city

# Definir a mensagem de acordo com o horário do dia
if 7 <= hora.hour < 12:
    mensagem = "Bom Dia"
elif 12 <= hora.hour < 18:
    mensagem = "Boa Tarde"
else:
    mensagem = "Boa Noite"

# Criar o texto do QR Code com as informações
texto = f"{mensagem}\nEste QR Code foi gerado em {hora.strftime('%d/%m/%Y %H:%M:%S')} no local {local}."

# Criar o QR Code com o texto
qr = qrcode.QRCode()
qr.add_data(texto)
qr.make(fit=True)

# Salvar o QR Code como uma imagem
img = qr.make_image(fill_color="black", back_color="white")

# Criar um novo objeto PIL Image para adicionar o texto
img_with_text = Image.new('RGB', (img.width, img.height + 60), color = (255, 255, 255))
d = ImageDraw.Draw(img_with_text)

# Adicionar o texto acima do QR Code com gradiente de arco-íris
font = ImageFont.load_default()
colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
x = 10
for i, letter in enumerate(texto):
    d.text((x,10), letter, font=font, fill=colors[i % len(colors)])
    x += d.textsize(letter, font=font)[0]

# Colocar o QR Code abaixo do texto
img_with_text.paste(img, (0, 60))

# Salvar a imagem final
img_with_text.save('qrcode_mensagem.png')

# Exibir o QR Code na tela
img_with_text.show()

# Criar o QR Code para a URL
url = "https://www.google.com"
qr_url = qrcode.QRCode()
qr_url.add_data(url)
qr_url.make(fit=True)

# Salvar o QR Code da URL como uma imagem
img_url = qr_url.make_image(fill_color="black", back_color="white")
img_url.save("qrcode_url.png")

# Exibir o QR Code da URL na tela
img_url.show()