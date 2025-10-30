# 🖼️ Image → ASCII Art (Python + Streamlit)

Convierte imágenes en arte ASCII directamente desde tu navegador usando **Streamlit**.  
Permite ajustar resolución, contraste, suavizado y rampas de caracteres para obtener resultados más o menos detallados.

---

# Demo
You can try it here [https://imagetoascii.streamlit.app](https://imagetoascii.streamlit.app)

---

## 📂 Estructura del proyecto

```
image-to-ascii/
├─ ascii_core.py          # Conversión imagen → ASCII
├─ preprocess.py          # Preprocesado (escala de grises, blur, resize)
├─ ramps.py               # Rampas de caracteres (presets)
├─ streamlit_app.py       # Interfaz principal Streamlit
├─ requirements.txt
└─ samples/
   └─ example.jpg
```

---

## ⚙️ Requisitos

Python **3.9 o superior** y las librerías indicadas en `requirements.txt`:

```txt
numpy>=1.24
Pillow>=10.0
streamlit>=1.28
```

---

## 🚀 Instalación

### 🧠 Crear entorno virtual

**Linux / macOS**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 📦 Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

Ejecuta la aplicación Streamlit desde la carpeta del proyecto:

```bash
streamlit run ui_streamlit.py
```

Luego abre la URL que aparece en consola (normalmente [http://localhost:8501](http://localhost:8501))

> 💡 En WSL, abre la URL en tu navegador de Windows.

---

## 🧭 Uso de la aplicación

1. **Sube una imagen** (`.jpg`, `.jpeg`, `.png`).
2. Ajusta los **controles** (ahora en barra lateral o columna lateral):
   - 🎚️ **Ancho (cols):** número de caracteres por línea.  
   - 🧮 **Corrección de aspecto:** compensa la altura de los caracteres (0.45–0.55 ideal).  
   - 🌈 **Gamma:** controla contraste/luminosidad percibida.  
   - 💧 **Suavizado:** desenfoque previo (reduce ruido).  
   - 🔳 **Bloque de muestreo:** promedio de píxeles por carácter (más alto = menos detalle).  
   - 🔁 **Invertir:** invierte la rampa de brillo.  
   - 🎨 **Preset:** elige la rampa de caracteres (`classic`, `detailed`, `blocks`).
3. Pulsa **Descargar .txt** para guardar el arte ASCII.

---

## 🧠 Detalles técnicos

- Conversión basada en brillo medio de bloques de píxeles.  
- Corrección de aspecto configurable (por defecto `0.5` para fuentes monoespaciadas).  
- `preprocess.py`:
  - Convierte a escala de grises (`L`)
  - Aplica reducción de tamaño si la imagen es muy grande
  - Filtro Gaussiano opcional (`blur`)  
- `ascii_core.py`:
  - Calcula medias por bloques  
  - Aplica curva `gamma`  
  - Mapea cada nivel de brillo a un carácter de la rampa

---

## 🧩 Ejemplo rápido

```bash
streamlit run streamlit_app.py
```

Carga `samples/example.jpg` y prueba:
- Ancho: `60`
- Aspecto: `0.5`
- Bloque: `4`
- Gamma: `1.0`

Resultado:

```
                     .:-=++*****++=-:.                      
                .:=*#@@@@@###%###@@@@@#*=:.                 
             .-*@@@@%+-:..       ..:-+*#@@@*-.              
           .+#@@%=:.                   .:=%@@@+.            
         .+@@@+:       ..:-===--:..        .+@@@*.          
       .=@@@=.     .-+++=-:...::-=+++-.      .=@@@=.        
      .*@@*.    .-*+:.              .:++-.     .*@@%.       
     .%@@=.   .=*-.     .:-=====-:.    .-*-      =@@#.      
    .%@@=    .%=.   .-+++=::....:=++=.   .=*.     -@@%.     
    +@@+    :%:   .=*=..=++++++++=. :*+.   :%.     =@@+     
   .@@#.   .#:   .*-..**:....   .:*+. -%.   :%.    .#@@:    
   =@@=    *=   .%: :#: -*++*+.    ++  -%.   +=     =@@+    
   *@@:   .@.   -* .#: :%.  .@.    .#  .#:   :%     :@@%    
   %@@.   .@    =+ .@. +=   -#.    :%  .#.   .#     .@@%    
   *@@:   .@.   :%..%- -*  .#-     +=  :#.   .%     :@@%    
   =@@=    %=    ++..%--*  =*     -%. .%-    ==     =@@+    
   .@@#.   :#.    :++%.%:  -%. .:++. .*=    .%.    .#@@.    
    +@@+    =%.       -%  -::=++=. .=%-    .%:     +@@+     
    .%@@=    -%:      %: .@+++==++++:.    :%:     -@@%.     
     .%@@=.   .**.   :%. ++  .....      :++.     =@@#.      
      .*@@%.    :**-.+= :#.          .-*+.     .*@@*.       
        =@@@+.    .-+%-:#:     ..:-+++-.     .=@@@=.        
         .+@@@+:       :=++++++++=:.       :+@@@+.          
           .+#@@%+:.                   .:=%@@#+.            
             .-*#@@@%+-:..       ..:-+%@@@@*-.              
                .:=*#@@@@@#######@@@@@#*=:.                 
                     .:-=++*****++=-:.
```

---

## 💡 Sugerencias

- Usa imágenes **en escala de grises o alto contraste** para mejores resultados.  
- Reduce el **ancho** si tu terminal o ventana de navegador corta líneas.  
- Ajusta `aspect_correction` si notas que el ASCII se ve “aplastado” o “alargado”.  
- Experimenta con diferentes rampas de caracteres en `ramps.py`.
