from PIL import Image, ImageFilter

def preprocess(src, max_size=800, blur=0.5):
	# Abrir imagen
	img = Image.open(src).convert("L")  # "L" = escala de grises
	
	# Reducción de tamaño
	w, h = img.size
	if max(w, h) > max_size:
		scale = max_size / max(w, h)
		img = img.resize((int(w * scale), int(h * scale)))

	# Filtro para suavizar (reduce ruido)
	img = img.filter(ImageFilter.GaussianBlur(blur))

	return img