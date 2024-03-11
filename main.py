# Importar as bibliotecas necessárias
import qrcode
import datetime
import geocoder
from PIL import Image, ImageDraw, ImageFont

# Criar uma nova imagem em branco
width, height = 500, 500
background = (255, 255, 255)
img = Image.new('RGB', (width, height), background)

# Criar um objeto ImageDraw para desenhar na imagem
draw = ImageDraw.Draw(img)

# Definir a fonte
font = ImageFont.load_default()

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
texto = f"{mensagem}\nEste QR Code foi gerado em {hora.strftime('%d/%m/%Y %H:%M:%S')}\n no local: {local}."

# Desenhar o texto na imagem
draw.text((10, 10), texto, fill="black", font=font)

# Criar o QR Code para a URL
url = "https://github.com/Cavalchi"
qr_url = qrcode.QRCode()
qr_url.add_data(url)
qr_url.make(fit=True)

# Salvar o QR Code da URL como uma imagem
img_url = qr_url.make_image(fill_color="black", back_color="white")

# Redimensionar o QR Code para que ele caiba na imagem
img_url = img_url.resize((200, 200))

# Calcular a posição do QR Code para que ele fique no centro da imagem
qr_x = (width - img_url.width) / 2
qr_y = (height - img_url.height) / 2

# Colar o QR Code na imagem
img.paste(img_url, (int(qr_x), int(qr_y)))

# Salvar a imagem
img.save("imagem_com_texto_e_qrcode.png")

# Exibir a imagem na tela
img.show()
