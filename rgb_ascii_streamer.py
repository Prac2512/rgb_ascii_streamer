import cv2
import pygame
import numpy as np
from PIL import Image
import time

# --- Configuration ---
ASCII_CHARS = "@%#*+=-:. "
RESIZE_FACTOR = 0.15
FONT_SIZE = 10
VIDEO_OUTPUT = False  # Set to True to save to .avi
VIDEO_FILENAME = "ascii_output.avi"

# --- Initialize Webcam ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

# --- Initialize Pygame ---
pygame.init()
pygame.display.set_caption("🎨 Colored ASCII Webcam Viewer (ESC to Quit)")
font = pygame.font.SysFont("Courier", FONT_SIZE, bold=True)
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# --- Initialize Video Writer (Optional) ---
writer = None
if VIDEO_OUTPUT:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    writer = cv2.VideoWriter(VIDEO_FILENAME, fourcc, 10, (800, 600))

def frame_to_ascii_colored(image):
    """Convert RGB PIL image to a 2D array of (char, color) tuples."""
    width, height = image.size
    new_w = int(width * RESIZE_FACTOR)
    new_h = int(height * RESIZE_FACTOR * 0.55)
    image = image.resize((new_w, new_h))
    pixels = list(image.getdata())
    ascii_image = []

    for y in range(new_h):
        line = []
        for x in range(new_w):
            r, g, b = pixels[y * new_w + x]
            brightness = int(0.299 * r + 0.587 * g + 0.114 * b)
            char = ASCII_CHARS[int((brightness / 255) * (len(ASCII_CHARS) - 1))]
            line.append((char, (r, g, b)))
        ascii_image.append(line)
    return ascii_image

# --- Main Loop ---
clock = pygame.time.Clock()
running = True

while running:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert frame to PIL Image
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(frame_rgb)

    ascii_art = frame_to_ascii_colored(pil_img)

    screen.fill((0, 0, 0))
    for y, line in enumerate(ascii_art):
        for x, (char, color) in enumerate(line):
            surface = font.render(char, True, color)
            screen.blit(surface, (x * FONT_SIZE * 0.6, y * FONT_SIZE))

    pygame.display.flip()

    if VIDEO_OUTPUT:
        ascii_surface = pygame.display.get_surface()
        video_frame = pygame.surfarray.array3d(ascii_surface)
        video_frame = np.transpose(video_frame, (1, 0, 2))  # Convert to OpenCV format
        video_frame = cv2.resize(video_frame, (800, 600))
        video_frame = cv2.cvtColor(video_frame, cv2.COLOR_RGB2BGR)
        writer.write(video_frame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    clock.tick(15)  # Limit to ~15 FPS

# --- Cleanup ---
cap.release()
if writer:
    writer.release()
pygame.quit()
print("Exited cleanly.")

# --- End of Program ---