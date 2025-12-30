from PIL import Image, ImageDraw, ImageFont

W, H = 800, 240
img = Image.new('RGB', (W, H), color=(255,255,255))
d = ImageDraw.Draw(img)

# Basit metin; sistemde Arial/DejaVuSans olabilir, fallback kullanılır.
try:
    font = ImageFont.truetype('arial.ttf', 32)
except Exception:
    font = ImageFont.load_default()

text = 'Golge128 Sifreleme\nÇalıştırma Örneği\nÇıkış: Başarılı'
# Çok satırlı metin çizimi
d.multiline_text((20, 40), text, fill=(20,20,20), font=font, spacing=10)

img.save('code.jpeg', 'JPEG')
print('code.jpeg oluşturuldu')
