
# Colored ASCII Webcam Viewer

A real-time colored ASCII art webcam viewer built with Python using `OpenCV`, `Pillow`, and `pygame`.  
This program captures your webcam feed, converts it frame-by-frame to colored ASCII art, and renders it in a resizable Pygame window.

---

## Features

- **Real-time webcam capture** using OpenCV.
- **Colored ASCII art rendering** using RGB values mapped to ASCII characters.
- Adjustable resize factor and font size.
- Optional video recording of the ASCII output.
- Clean GUI window with ESC key to quit.
- Cross-platform support (Windows, macOS, Linux).

---

## Requirements

- Python 3.6+
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Pillow](https://pypi.org/project/Pillow/)
- [pygame](https://pypi.org/project/pygame/)
- numpy

---

## Installation

Install dependencies using pip:

```bash
pip install opencv-python pillow pygame numpy
````

---

## Usage

Run the script:

```bash
python rgb_ascii_streamer.py
```

* The program opens a resizable window showing your webcam feed converted into colored ASCII art.
* Press **ESC** or close the window to exit.
* To enable video recording, set `VIDEO_OUTPUT = True` in the script (this will save `ascii_output.avi` in the current directory).

---

## Configuration

Inside `rgb_ascii_streamer.py`, you can adjust:

* `ASCII_CHARS`: Characters used for ASCII art, from dark to light.
* `RESIZE_FACTOR`: Scale factor to resize the webcam image before conversion (affects quality and performance).
* `FONT_SIZE`: Font size of rendered ASCII characters.
* `VIDEO_OUTPUT`: Enable/disable saving the output to a video file.
* `VIDEO_FILENAME`: Name of the output video file.

---

## How It Works

1. Captures a frame from the webcam.
2. Converts the frame to a PIL image and resizes it.
3. Maps each pixel to an ASCII character based on brightness.
4. Colors the ASCII character based on the pixel's RGB values.
5. Renders the colored ASCII art in the Pygame window.
6. Optionally saves the output to a video file.

---

## Troubleshooting

* **Webcam not accessible:** Ensure your webcam is connected and not used by another app.
* **Pygame window is blank or flickering:** Try adjusting `RESIZE_FACTOR` or `FONT_SIZE` for your screen resolution.
* **Permission errors when saving video:** Check file permissions and whether a file with the same name is open.

---

## License

This project is licensed under the MIT License.

---
## Made with ❤️ and passion for creativity by Prachi Patil

Thank you for checking out this project! Feel free to use, modify, and share.  
Let's bring art and code together! 🎨✨
----
## Author

Prachi Patil
Email: [patilprachi2598@gmail.com](mailto:patilprachi2598@gmail.com)

---

Feel free to contribute or raise issues!

