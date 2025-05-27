
# QR Code Generator with Logo Support

A simple and lightweight Python desktop application that generates QR codes from user input. Includes an optional feature to overlay a custom logo at the center of the QR code. Built using Tkinter for GUI and `qrcode` for QR code generation.

## ✨ Features

- Generate QR codes from text or URLs
- Add a logo/image to the center of the QR code (optional)
- Save generated QR codes as PNG files
- Simple and user-friendly GUI interface
- Compatible with Windows

## 🖥️ Preview

![Screenshot](./assets/screenshot.png) <!-- Replace with an actual image path if available -->

## 🛠️ Technologies Used

- Python 3.x
- Tkinter
- qrcode
- Pillow (PIL)

## 📦 Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/TechnocoolMW/QR-generator.git
   cd QR-generator
````

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

   Or install them manually:

   ```bash
   pip install qrcode[pil] pillow
   ```

3. **Run the app:**

   ```bash
   python qr_generator.py
   ```

## 🧾 How to Use

1. Enter the text or URL you want to encode.
2. (Optional) Choose a logo image from your computer.
3. Click "Generate QR Code".
4. Click "Save QR Code" to download the PNG file.

## 📂 Project Structure

```
QRGenerator/
├── qr_generator.py         # Main app file
├── .gitignore
├── logos/                  # Optional logo images
├── dist/                   # Compiled .exe files (if using PyInstaller)
└── README.md
```

## 📑 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

* [qrcode](https://pypi.org/project/qrcode/)
* [Pillow](https://python-pillow.org/)
* [PyInstaller](https://pyinstaller.org/) for `.exe` packaging

````

---



