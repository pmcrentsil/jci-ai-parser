from utils.azure_ocr import extract_text_and_polygons
from utils.cropper import crop_diagram
from utils.vision_inference import analyze_with_vision

pdf_file = "input/Example 4.pdf"  # Change as needed
output_path = "output/crop_output.png"

pages = extract_text_and_polygons(pdf_file)

if pages:
    first_match = pages[0]
    cropped_img = crop_diagram(pdf_file, first_match["page"], first_match["polygon"])
    cropped_img.save(output_path)
    print("Cropped image saved. Sending to GPT-4 Vision...")

    result = analyze_with_vision(output_path)
    print("\n--- Extracted Sequence of Operation ---\n")
    print(result)
else:
    print("No 'Sequence of Operation' text found.")