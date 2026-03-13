import cv2
import numpy as np
from typing import List, Tuple, Optional, Union


class ImageIO:
    """
    Kelas untuk menangani Input dan Output gambar.
    """

    def load(self, path: str, flag: int = cv2.IMREAD_COLOR) -> np.ndarray:
        """Membaca gambar dari file."""
        img = cv2.imread(path, flag)
        if img is None:
            raise FileNotFoundError(f"Gambar tidak ditemukan di path: {path}")
        return img

    def save(self, path: str, image: np.ndarray) -> bool:
        """Menyimpan gambar ke file."""
        success = cv2.imwrite(path, image)
        if not success:
            raise IOError("Gagal menyimpan gambar.")
        return success

    def show(
        self, title: str, image: np.ndarray, wait_time: int = 0
    ) -> None:
        """Menampilkan gambar di jendela popup."""
        cv2.imshow(title, image)
        cv2.waitKey(wait_time)


class ImagePreprocessor:
    """
    Kelas untuk preprocessing dasar seperti resizing dan konversi warna.
    """

    def resize(
        self,
        image: np.ndarray,
        width: Optional[int] = None,
        height: Optional[int] = None,
        inter: int = cv2.INTER_AREA,
    ) -> np.ndarray:
        """Mengubah ukuran gambar dengan menjaga aspek rasio."""
        dim = None
        (h, w) = image.shape[:2]

        if width is None and height is None:
            return image

        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)

    def to_grayscale(self, image: np.ndarray) -> np.ndarray:
        """Mengubah gambar berwarna menjadi hitam putih (Grayscale)."""
        if len(image.shape) == 2:
            return image
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def to_hsv(self, image: np.ndarray) -> np.ndarray:
        """Mengubah gambar ke ruang warna HSV."""
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def blur(
        self, image: np.ndarray, kernel_size: Tuple[int, int] = (5, 5)
    ) -> np.ndarray:
        """Menerapkan Gaussian Blur untuk mengurangi noise."""
        return cv2.GaussianBlur(image, kernel_size, 0)

    def normalize(self, image: np.ndarray) -> np.ndarray:
        """Normalisasi pixel ke range 0-1 (float)."""
        return image.astype("float") / 255.0


class FeatureExtractor:
    """
    Kelas untuk mendeteksi fitur seperti tepi, kontur, dan garis.
    """

    def detect_edges(
        self,
        image: np.ndarray,
        low_thresh: int = 30,
        high_thresh: int = 150,
    ) -> np.ndarray:
        """Mendeteksi tepi menggunakan algoritma Canny."""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        return cv2.Canny(gray, low_thresh, high_thresh)

    def find_contours(
        self, image: np.ndarray
    ) -> Tuple[List[np.ndarray], np.ndarray]:
        """Menemukan kontur objek dalam gambar biner/edges."""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        _, thresh = cv2.threshold(
            gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        return contours, thresh

    def draw_contours(
        self,
        original_image: np.ndarray,
        contours: List[np.ndarray],
        color: Tuple[int, int, int] = (0, 255, 0),
        thickness: int = 2,
    ) -> np.ndarray:
        """Menggambar kontur di atas gambar asli."""
        output = original_image.copy()
        cv2.drawContours(output, contours, -1, color, thickness)
        return output

    def detect_circles(
        self,
        image: np.ndarray,
        min_dist: int = 50,
        param1: int = 50,
        param2: int = 50,
        min_radius: int = 0,
        max_radius: int = 0,
    ) -> Optional[np.ndarray]:
        """Mendeteksi lingkaran menggunakan Hough Circle Transform."""
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        gray = cv2.medianBlur(gray, 5)
        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            1,
            min_dist,
            param1=param1,
            param2=param2,
            minRadius=min_radius,
            maxRadius=max_radius,
        )
        return circles


class ObjectAnalyzer:
    """
    Kelas untuk analisis objek sederhana seperti Bounding Box.
    """

    def get_bounding_boxes(
        self, contours: List[np.ndarray]
    ) -> List[Tuple[int, int, int, int]]:
        """Mengambil koordinat kotak pembatas (x, y, w, h) dari kontur."""
        boxes = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            # Filter objek terlalu kecil (noise)
            if w > 10 and h > 10:
                boxes.append((x, y, w, h))
        return boxes

    def draw_boxes(
        self,
        image: np.ndarray,
        boxes: List[Tuple[int, int, int, int]],
        color: Tuple[int, int, int] = (255, 0, 0),
        thickness: int = 2,
    ) -> np.ndarray:
        """Menggambar kotak pembatas pada gambar."""
        output = image.copy()
        for (x, y, w, h) in boxes:
            cv2.rectangle(output, (x, y), (x + w, y + h), color, thickness)
        return output
