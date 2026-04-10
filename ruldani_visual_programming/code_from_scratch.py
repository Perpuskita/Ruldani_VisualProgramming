from PIL import Image
import numpy as np
import os


class ImageIO:
    def __init__(self):
        pass

    def load(self, path: str) -> np.ndarray:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image file not found: {path}")

        try:
            with Image.open(path) as img:
                img = img.convert("RGB")  # Ensure consistent format
                return np.array(img)
        except Exception as e:
            raise Exception(f"Failed to load image: {e}")

    def save(self, path: str, image: np.ndarray, type_image: str = "PNG") -> Image.Image:
        try:
            # Ensure correct dtype and range
            if image.dtype == np.float32 or image.dtype == np.float64:
                image = (image * 255).astype(np.uint8)
            elif image.dtype != np.uint8:
                image = image.astype(np.uint8)

            # Handle grayscale
            if image.ndim == 2:
                pil_image = Image.fromarray(image, mode='L')
            elif image.ndim == 3 and image.shape[2] == 3:
                pil_image = Image.fromarray(image, mode='RGB')
            elif image.ndim == 3 and image.shape[2] == 4:
                pil_image = Image.fromarray(image, mode='RGBA')
            else:
                raise ValueError("Unsupported image shape for saving.")

            # Ensure directory exists
            os.makedirs(os.path.dirname(path) or '.', exist_ok=True)

            # Save image
            pil_image.save(path, format=type_image.upper())
            return pil_image

        except Exception as e:
            raise Exception(f"Failed to save image: {e}")

    def show(self, title: str, image: np.ndarray) -> None:
        try:
            if image.dtype == np.float32 or image.dtype == np.float64:
                image = (image * 255).astype(np.uint8)
            elif image.dtype != np.uint8:
                image = image.astype(np.uint8)

            if image.ndim == 2:
                pil_image = Image.fromarray(image, mode='L')
            elif image.ndim == 3 and image.shape[2] == 3:
                pil_image = Image.fromarray(image, mode='RGB')
            elif image.ndim == 3 and image.shape[2] == 4:
                pil_image = Image.fromarray(image, mode='RGBA')
            else:
                raise ValueError("Unsupported image shape for display.")

            pil_image.title = title
            pil_image.show()

        except Exception as e:
            raise Exception(f"Failed to display image: {e}")

class ImageManip:
    def __init__(self):
        pass

    def _convolve_2d(self, image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
        """
        Helper function to perform 2D convolution on a single channel (2D array).
        Implemented manually using numpy padding and slicing to avoid scipy.
        """
        kh, kw = kernel.shape
        pad_h, pad_w = kh // 2, kw // 2
        
        # Padding image using 'reflect' mode to handle borders
        padded = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='reflect')
        
        h, w = image.shape
        output = np.zeros((h, w), dtype=np.float64)
        
        # Perform convolution by sliding the kernel over the padded image
        # Looping over kernel elements is faster than looping over pixels
        for i in range(kh):
            for j in range(kw):
                output += kernel[i, j] * padded[i:i+h, j:j+w]
                
        return output

    def kernel_manip(self, image: np.ndarray, kernel: np.ndarray) -> np.ndarray:

        if kernel.ndim != 2:
            raise ValueError("Kernel must be a 2D array.")

        if image.ndim == 2:
            # Grayscale
            return self._convolve_2d(image, kernel)
        
        elif image.ndim == 3:
            # Color (H, W, C)
            h, w, c = image.shape
            output = np.zeros((h, w, c), dtype=np.float64)
            for i in range(c):
                output[:, :, i] = self._convolve_2d(image[:, :, i], kernel)
            return output
        
        else:
            raise ValueError("Image must be 2D or 3D.")

    def gaussian_blur(self, image: np.ndarray, sigma: float = 1.0, kernel_size: int = 0) -> np.ndarray:

        if kernel_size == 0:
            kernel_size = int(6 * sigma + 1)
        
        # Ensure kernel size is odd
        if kernel_size % 2 == 0:
            kernel_size += 1
            
        # Create 1D Gaussian kernel
        ax = np.linspace(-(kernel_size // 2), kernel_size // 2, kernel_size)
        xx, yy = np.meshgrid(ax, ax)
        kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
        kernel /= np.sum(kernel)  # Normalize kernel

        return self.kernel_manip(image, kernel)

    def gray_scale(self, image: np.ndarray, cfg: int = 10) -> np.ndarray:

        if image.ndim == 2:
            return image

        if image.ndim != 3 or image.shape[2] not in [3, 4]:
            raise ValueError("Image must have 3 (RGB) or 4 (RGBA) channels.")

        # Drop alpha channel if present
        if image.shape[2] == 4:
            image = image[:, :, :3]

        # Convert to float for calculation if needed
        if image.dtype == np.uint8:
            image = image.astype(np.float64) / 255.0

        # Luminance formula
        gray = 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 2]

        # Convert back to uint8
        return (gray * 255).astype(np.uint8)
    

class NeuralNetwork:
    def __init__(self):
        pass

    def fully_connected(self, input_layer: np.ndarray) -> np.ndarray:
        return None
    
    def convolutional_nn(self, input_layer: np.ndarray) -> np.ndarray:
        return None

    def activation_layer(self, input_layer: np.ndarray) -> np.ndarray:
        return None