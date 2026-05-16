from PIL import Image
import os

def convert_png_to_ico(input_path, output_path):
    print(f"Converting {input_path} to {output_path}...")
    try:
        img = Image.open(input_path)
        # Save as ICO with standard sizes
        img.save(output_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
        print("Conversion successful!")
    except Exception as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    input_file = "cloudmesh_ai_theme/assets/favicon-2.png"
    output_file = "cloudmesh_ai_theme/assets/favicon.ico"
    convert_png_to_ico(input_file, output_file)