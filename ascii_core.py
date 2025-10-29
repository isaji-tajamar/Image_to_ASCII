import numpy as np
import ramps as r

def image_to_ascii(img, width=100, invert=False, block_size=4, ramp=r.ramp_classic, gamma=1.0, aspect_correction=0.5):
	w, h = img.size
	new_h = max(1, int(width * h / w * aspect_correction))
	img = img.resize((width * block_size, new_h * block_size))

	a = np.array(img, dtype=np.float32)
	if gamma and gamma > 0:
		a = np.clip((a / 255.0) ** (1.0 / gamma), 0, 1) * 255.0

	H = (a.shape[0] // block_size) * block_size
	W = (a.shape[1] // block_size) * block_size
	a = a[:H, :W]
	a = a.reshape(H // block_size, block_size, W // block_size, block_size).mean(axis=(1, 3))

	idx = (a * (len(ramp) - 1) / 255.0).astype(int)
	if invert:
		idx = (len(ramp) - 1) - idx
	chars = np.array(list(ramp))
	mapped = chars[idx]
	return "\n".join("".join(row) for row in mapped)
