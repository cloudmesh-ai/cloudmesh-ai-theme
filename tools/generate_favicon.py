from PIL import Image
import os

def create_favicon(input_path, output_path):
    print(f"Processing {input_path}...")
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    # Find the most common color to treat as background
    color_counts = {}
    for item in datas:
        color_counts[item] = color_counts.get(item, 0) + 1
    
    bg_color = max(color_counts, key=color_counts.get)
    print(f"Detected background color: {bg_color}")

    new_data = []
    for item in datas:
        # Make background transparent
        if item == bg_color:
            new_data.append((0, 0, 0, 0))
            continue
        
        # Calculate brightness to distinguish between clouds and text
        # item is (R, G, B, A)
        brightness = (item[0] * 299 + item[1] * 587 + item[2] * 114) / 1000
        
        if brightness > 128:
            # Light color -> White cloud
            new_data.append((255, 255, 255, 255))
        else:
            # Dark color -> Black AI text
            new_data.append((0, 0, 0, 255))

    img.putdata(new_data)
    
    # Save as ICO
    img.save(output_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    print(f"Saved favicon to {output_path}")

if __name__ == "__main__":
    input_file = "cloudmesh_ai_theme/assets/favicon.png"
    output_file = "cloudmesh_ai_theme/assets/favicon.ico"
    create_favicon(input_file, output_file)