from PIL import Image
import os

output_folder = "compressed_webp"
os.makedirs(output_folder, exist_ok=True)

supported_formats = (
    ".jpg", ".jpeg", ".png", ".bmp",
    ".gif", ".tiff", ".tif", ".webp"
)

for filename in os.listdir("."):
    if filename.lower().endswith(supported_formats):
        try:
            img = Image.open(filename)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")

            output_name = os.path.splitext(filename)[0] + ".webp"
            output_path = os.path.join(output_folder, output_name)

            img.save(
                output_path,
                format="WEBP",
                quality=85,  # 80-90 is usually a good balance
                method=6
            )

            orig_size = os.path.getsize(filename) / 1024
            new_size = os.path.getsize(output_path) / 1024

            print(
                f"{filename}: "
                f"{orig_size:.1f} KB -> {new_size:.1f} KB "
                f"({(1 - new_size/orig_size)*100:.1f}% reduction)"
            )

        except Exception as e:
            print(f"Error: {filename} - {e}")

print("Done!")