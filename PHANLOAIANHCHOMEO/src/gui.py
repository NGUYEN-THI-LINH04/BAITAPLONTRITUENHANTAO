import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# ✅ IMPORT ĐÚNG THEO CẤU TRÚC
from src.predict import predict_image


class DogCatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🐶🐱 Phân loại Chó - Mèo")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.label = tk.Label(
            root,
            text="Ứng dụng phân loại ảnh Chó / Mèo",
            font=("Arial", 18, "bold")
        )
        self.label.pack(pady=20)

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 16),
            fg="blue"
        )
        self.result_label.pack(pady=10)

        self.btn_choose = tk.Button(
            root,
            text="📂 Chọn ảnh",
            font=("Arial", 14),
            command=self.choose_image,
            width=15
        )
        self.btn_choose.pack(pady=20)

    def choose_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.png *.jpeg")]
        )

        if not file_path:
            return

        img = Image.open(file_path)
        img = img.resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)

        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

        result, confidence = predict_image(file_path)

        self.result_label.config(
            text=f"Kết quả: {result}\nĐộ tin cậy: {confidence:.2f}%"
        )
