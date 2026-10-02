from PIL import Image
import os

# Create output folder
output_folder = "converted_png"
os.makedirs(output_folder, exist_ok=True)

# Supported input formats
supported_formats = (
    ".jpg", ".jpeg", ".bmp", ".gif",
    ".tiff", ".tif", ".webp"
)

# Convert all images in the current folder
for filename in os.listdir("."):
    if filename.lower().endswith(supported_formats):
        try:
            img = Image.open(filename)

            # Convert palette images if needed
            if img.mode == "P":
                img = img.convert("RGBA")

            # Preserve original filename, change extension to .png
            png_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, png_filename)

            img.save(output_path, "PNG")

            print(f"✓ Converted: {filename} -> {output_path}")

        except Exception as e:
            print(f"✗ Failed: {filename} ({e})")

print(f"\nDone! All PNG files have been saved to '{output_folder}'")