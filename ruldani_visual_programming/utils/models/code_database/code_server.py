
###### Node interprenter ######

class interpreter_code:

    def __init__(self, name):
        self.name = name
        self.interpreter = self.get_interpreter()
        self.input = self.interpreter.input
        self.output = self.interpreter.output

    #  Controller
    def get_interpreter( self ):

        if self.name == "folder":
            return Preferences_Folder("folder")
        elif self.name == "gdrive folder":
            return Preferences_GDrive("gdrive")
        elif self.name == "pembentukan citra":
            return Preferences_PembentukCitra("pembentukan citra")
        elif self.name == "analisa biner":
            return Preferences_Biner("analisa biner")
        elif self.name == "analisa abu":
            return Preferences_Abu("analisa abu")
        elif self.name == "transformasi fourier":
            return Preferences_Fourier("transformasi fourier")
        elif self.name == "deteksi tepi":
            return Preferences_Tepi("deteksi tepi")
        elif self.name == "ekstraksi_fitur":
            return Preferences_Efitur("ekstraksi_fitur")
        # else :
        #     print(f"inisialisasi node gagal")

###### Node interprenter for folder import #######

def folder_code(name, link):
    return f'''# baris untuk open folder \n{name} = '{link}'\n'''

class Preferences_Folder():
    def __init__(self, name):
        self.name = name
        self.link = "/content/test"
        self.header = []
        self.input = []
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["link", self.link]]
    
    def code_saver(self, load):
        return folder_code(self.name.replace(" ", "_"), self.link), self.name.replace(" ", "_"), self.header
     
    def update_data(self, name, link):
        self.name = name
        self.link = link

###### Node interprenter for gdrive folder import #######

def gdrive_code( name, link):
    return f'''
drive.mount('/content/drive')
{name} = '{link}'
'''

class Preferences_GDrive():
    def __init__(self, name):
        self.name = name
        self.link = '/content/drive/MyDrive/test'
        self.header = ["from google.colab import drive"]
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["link", self.link]]
    
    def code_saver(self, load):
        return gdrive_code(self.name.replace(" ", "_"), self.link), self.name.replace(" ", "_"), self.header
        
    def update_data(self, name, link):
        self.name = name
        self.link = link

###### Node interprenter for pembentukan citra #######

def preference_pembentukcitra(path):
    return f'''
def plot_show_rgb(image, counter, cmaps = None):
    
    plt.subplot((counter // 6) + 1, 6, counter % 6 + 1)
    if cmaps is not None:
        plt.imshow(image, cmap=cmaps)
    else:
        plt.imshow(image)
    
    plt.axis('off')

# Fungsi untuk melakukan transformasi Fourier pada gambar dalam folder
def transform_folder_images(folder_path):
    # Membuat figure baru di sini
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            
            plt.figure(figsize=(15,15)) 
            image_path = os.path.join(folder_path, filename)
            
            # Baca gambar dan lakukan Fourier Transform
            image = Image.open(image_path)
            image_rgb = image.convert('RGB')
            r,g,b = image_rgb.split()
            
            plot_show_rgb(image_rgb, 0)
            plot_show_rgb(r, 1, cmaps='Reds')
            plot_show_rgb(g, 2, cmaps='Greens')
            plot_show_rgb(b, 3, cmaps='Blues')
            
            image_gray = image.convert('L')     
            plot_show_rgb(image_rgb, 4)
            plot_show_rgb(image_gray.convert('RGB'), 5)
            plt.show()

transform_folder_images({path})'''

class Preferences_PembentukCitra():
    def __init__(self, name):
        self.name = name
        self.link = None
        self.framework = ["Pillow"]
        self.selected_framework = "Pillow"
        self.header = ["import matplotlib.pyplot as plt",
                       "import numpy as np",
                       "from PIL import Image"]
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["framework", self.framework, self.selected_framework]]
    
    def code_saver(self, load):

        addition = '''# baris untuk show analisis citra\n'''
        if self.selected_framework == "Pillow":
            return addition + preference_pembentukcitra(load), load, self.header
    
    def update_data(self, name, frameworks):
        self.name = name
        self.selected_framework = frameworks

###### Node interprenter for binary image #######

def analisa_biner(path) :
    return f'''
def citra_abu_folder_images(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            
            # Read the image and convert to grayscale
            image = Image.open(image_path).convert('L')
            image_np = np.array(image)  

            # Apply binary threshold
            _, citra_biner = cv2.threshold(image_np, 128, 255, cv2.THRESH_BINARY)
            Prepare images and titles for display
            images = [image_np, citra_biner]
            titles = ['Grayscale Image', 'Binary Image']
            
            # Display images using a loop
            plt.figure(figsize=(8, 4))
            for i in range(len(images)):
                plt.subplot(1, 2, i + 1)
                plt.imshow(images[i], cmap='gray')
                plt.title(titles[i])
                plt.axis('off')
                plt.tight_layout()
                plt.show()

# Run the function
citra_abu_folder_images({path})'''

class Preferences_Biner():
    def __init__(self, name):
        self.name = name
        self.link = None
        self.framework = ["OpenCV"]
        self.selected_framework = "OpenCV"
        self.header = ["import matplotlib.pyplot as plt", 
                       "import numpy as np", 
                       "import tkinter as tk",
                       "from PIL import Image"]
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["framework", self.framework, self.selected_framework]]
    
    def code_saver(self, load):
        return analisa_biner(load),load, self.header
    
    def update_data(self, name, frameworks):
        self.name = name
        self.selected_framework = frameworks

#analisa ABU

def analisa_abu(path):
    return f'''def citra_abu_folder_images(folder_path):\n\tfor filename in os.listdir(folder_path):\n\t\tif filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):\n\t\t\timage_path = os.path.join(folder_path, filename)\n\n\t\t\t# Read the image and convert to grayscale\n\t\t\timage = Image.open(image_path).convert('L')\n\t\t\timage_np = np.array(image)  # Convert to numpy array for compatibility with OpenCV\n\n\t\t\t# Apply binary threshold\n\t\t\t_, citra_biner = cv2.threshold(image_np, 128, 255, cv2.THRESH_BINARY)\n\n\t\t\t# Prepare images and titles for display\n\t\t\timages = [image_np, citra_biner]\n\t\t\ttitles = ['Grayscale Image', 'Binary Image']\n\n\t\t\t# Display images using a loop\n\t\t\tplt.figure(figsize=(8, 4))\n\t\t\tfor i in range(len(images)):\n\t\t\t\tplt.subplot(1, 2, i + 1)\n\t\t\t\tplt.imshow(images[i], cmap='gray')\n\t\t\t\tplt.title(titles[i])\n\t\t\t\tplt.axis('off')\n\n\t\t\tplt.tight_layout()\n\t\t\tplt.show()\n\n# Run the function\ncitra_abu_folder_images({path})'''

class Preferences_Abu():
    def __init__(self, name):
        self.name = name
        self.link = None
        self.framework = ["OpenCV"]
        self.selected_framework = "OpenCV"
        self.header = ['''import matplotlib.pyplot as plt''', '''import numpy as np''', '''import os''', '''from PIL import Image''']
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["framework", self.framework, self.selected_framework]]
    
    def code_saver(self, load):
        return analisa_abu(load), load, self.header
    
    def update_data(self, name, framework):
        self.name = name
        self.selected_framework = framework

# fourier

def preference_fourier(path):
    return f'''def plot_show(image, counter):\n\n\tplt.subplot((counter // 6) + 1, 6, counter % 6 + 1)\n\tplt.imshow(image, cmap='gray')\n\tplt.axis('off')\n\n# Fungsi untuk melakukan transformasi Fourier pada gambar dalam folder\ndef transform_fourier_folder_images(folder_path):\n\tcounter = 0\n\tplt.figure(figsize=(15, 10))  # Membuat figure baru di sini\n\n\tfor filename in os.listdir(folder_path):\n\t\tif filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):\n\n\t\t\timage_path = os.path.join(folder_path, filename)\n\n\t\t\t# Baca gambar dan lakukan Fourier Transform\n\t\t\timage = Image.open(image_path).convert('L')\n\t\t\timage_array = np.array(image)\n\t\t\tfourier_transform = np.fft.fft2(image_array)\n\t\t\tfourier_shifted = np.fft.fftshift(fourier_transform)\n\t\t\tmagnitude_spectrum = np.log(np.abs(fourier_shifted) + 1)\n\n\t\t\tplot_show(image, counter)\n\t\t\tplot_show(magnitude_spectrum, counter+1)\n\t\t\tcounter += 2\n\n\n\tplt.show()\n\ntransform_fourier_folder_images({path})'''

class Preferences_Fourier():
    def __init__(self, name):
        self.name = name
        self.link = None
        self.framework = ["PIL"]
        self.selected_framework = "PIL"
        self.header = ['''import matplotlib.pyplot as plt''', '''import numpy as np''', '''import os''', '''from PIL import Image''']
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["framework", self.framework, self.selected_framework]]
    
    def code_saver(self, load):
        if self.selected_framework == "PIL":
            return preference_fourier(load), load, self.header
    
    def update_data(self, name, frameworks):
        self.name = name
        self.selected_framework = frameworks


###### Node interprenter untuk deteksi tepi #######

def preference_deteksi_tepi( path ):
    return f'''# Fungsi untuk melakukan transformasi Fourier pada gambar dalam folder\ndef deteksi_tepi_folder_images(folder_path):\n\n\tfor filename in os.listdir(folder_path):\n\t\tif filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):\n\t\t\timage_path = os.path.join(folder_path, filename)\n\n\t\t\t# Baca gambar dan lakukan Fourier Transform\n\t\t\timage = Image.open(image_path).convert('L')\n\t\t\timage_np = np.array(image)  # Konversi ke numpy array untuk kompatibilitas dengan cv2\n\n\t\t\t# 1. Deteksi Tepi dengan Metode Canny\n\t\t\tedges_canny = cv2.Canny(image_np, 100, 200)\n\n\t\t\t# 2. Deteksi Tepi dengan Metode Sobel (menggunakan gradien)\n\t\t\tsobel_x = cv2.Sobel(image_np, cv2.CV_64F, 1, 0, ksize=3)  # Gradien di arah X\n\t\t\tsobel_y = cv2.Sobel(image_np, cv2.CV_64F, 0, 1, ksize=3)  # Gradien di arah Y\n\t\t\tsobel_edges = cv2.magnitude(sobel_x, sobel_y)  # Menggabungkan gradien X dan Y\n\n\t\t\t# 3. Deteksi Tepi dengan Metode Laplacian\n\t\t\tlaplacian = cv2.Laplacian(image_np, cv2.CV_64F)\n\t\t\tlaplacian_edges = np.uint8(np.absolute(laplacian))  # Menyusun kembali hasilnya ke format gambar\n\n\t\t\t# Simpan hasil deteksi tepi ke dalam daftar\n\t\t\ttitles = [\"Gambar Asli\", \"Deteksi Tepi Canny\", \"Deteksi Tepi Sobel\", \"Deteksi Tepi Laplacian\", \"Gradien Sobel X\", \"Gradien Sobel Y\"]\n\t\t\timages = [\n\t\t\t\timage_np,\n\t\t\t\tedges_canny,\n\t\t\t\tsobel_edges,\n\t\t\t\tlaplacian_edges,\n\t\t\t\tnp.uint8(np.absolute(sobel_x)),\n\t\t\t\tnp.uint8(np.absolute(sobel_y))\n\t\t\t]\n\n\t\t\t# Tampilkan hasilnya menggunakan loop\n\t\t\tplt.figure(figsize=(12, 8))\n\t\t\tfor i in range(len(images)):\n\t\t\t\tplt.subplot(2, 3, i + 1)\n\t\t\t\tplt.imshow(images[i], cmap='gray')\n\t\t\t\tplt.title(titles[i])\n\t\t\t\tplt.axis('off')\n\n\t\t\tplt.tight_layout()\n\t\t\tplt.show()\n\ndeteksi_tepi_folder_images({path})'''

class Preferences_Tepi():
    def __init__(self, name):
        self.name = name
        self.link = None
        self.framework = ["OpenCV"]
        self.selected_framework = "OpenCV"
        self.header = ['''import matplotlib.pyplot as plt''', '''import numpy as np''', '''import cv2''', '''import os''', '''from PIL import Image''']
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["framework", self.framework, self.selected_framework]]
    
    def code_saver(self, load):
        return preference_deteksi_tepi(load),load, self.header
    
    def update_data(self, name, frameworks):
        self.name = name
        self.selected_framework = frameworks

###### Node interprenter untuk ekstraksi fitur #######

def ekstrak_fitur_opencv(path):
    return f'''def plot_show(image, counter):\n\n\tplt.subplot((counter // 6) + 1, 6, counter % 6 + 1)\n\tplt.imshow(image, cmap='gray')\n\tplt.axis('off')\n\n# Fungsi untuk menghitung GLCM\ndef compute_glcm(image, dx, dy):\n\tmax_gray = 256\n\tglcm = np.zeros((max_gray, max_gray), dtype=int)\n\trows, cols = image.shape\n\n\tfor i in range(rows - dx):\n\t\tfor j in range(cols - dy):\n\t\t\tintensity1 = image[i, j]\n\t\t\tintensity2 = image[i + dx, j + dy]\n\t\t\tglcm[intensity1, intensity2] += 1\n\n\t# Normalisasi GLCM agar menjadi probabilitas\n\tglcm = glcm / np.sum(glcm)\n\treturn glcm\n\ndef printout_matrix(matrix):\n\tfor row in matrix:\n\t\tprint(\"\\n\")\n\t\tprint(row[4], \"\\n\")\n\t\tprint(\"Contrast :\", row[0])\n\t\tprint(\"Homogeneity :\", row[1])\n\t\tprint(\"Energy :\", row[2])\n\t\tprint(\"Entropy :\", row[3], \"\\n\")\n\ndef folder_ekstraksi_fitur(folder_path):\n\tcounter = 0\n\tshow_matrix = []\n\tplt.figure(figsize=(15, 10))\n\tfor filename in os.listdir(folder_path):\n\t\tif filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):   \n\t\t\timage_path = os.path.join(folder_path, filename)\n\t\t\timage = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)\n\t\t\tplot_show(image, counter)\n\t\t\tcounter += 1\n\n\t\t\tdx, dy = 1, 0  # Arah horizontal\n\t\t\tglcm = compute_glcm(image, dx, dy)\n\n\t\t\tcontrast = np.sum((np.arange(glcm.shape[0])[:, None] - np.arange(glcm.shape[1]))**2 * glcm)\n\t\t\thomogeneity = np.sum(glcm / (1.0 + (np.arange(glcm.shape[0])[:, None] - np.arange(glcm.shape[1]))**2))\n\t\t\tenergy = np.sum(glcm ** 2)\n\t\t\tentropy = -np.sum(glcm * np.log2(glcm + 1e-10))  # Tambahkan 1e-10 untuk mencegah log(0)\n\t\t\tshow_matrix.append([contrast, homogeneity, energy, entropy, filename])\n\n\t\tif counter % 6 == 0:\n\t\t\tplt.show()\n\t\t\tcounter = 0\n\t\t\tprintout_matrix(show_matrix)\n\t\t\tplt.figure(figsize=(15, 10))\n\n\n\tif counter != 0:\n\t\tplt.show()\n\t\tprintout_matrix(show_matrix)\n\nfolder_ekstraksi_fitur({path})'''

class Preferences_Efitur():
    def __init__(self, name):
        self.name = name
        self.link = None
        self.framework = ["OpenCV"]
        self.selected_framework = "OpenCV"
        self.header = ['''import matplotlib.pyplot as plt''','''from PIL import Image''','''import numpy as np''', '''import os''']
        self.input = ["path"]
        self.output = ["path"]

    def atribute(self):
        return [["nama", self.name], ["framework", self.framework, self.selected_framework]]
    
    def code_saver(self, load):
        if self.selected_framework == "OpenCV":
            return ekstrak_fitur_opencv(load), load, self.header
        
    def update_data(self, name, frameworks):
        self.name = name
        self.selected_framework = frameworks
