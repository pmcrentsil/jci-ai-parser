# 🔧 JCI Sequence Extractor

This tool extracts **"Sequence of Operation"** steps from engineering diagrams in PDFs using:
- Azure Document Intelligence (`prebuilt-layout` OCR)
- Cropping of detected regions from the PDF
- GPT-4 Vision via Azure OpenAI to understand and return the sequence in structured text

---

## 📁 Folder Structure

```
jci-sequence-extractor/
├── main_pipeline.py                  # Entry point for running the pipeline
├── config.py                         # Your Azure credentials and model deployment
├── requirements.txt                  # All Python dependencies
├── utils/
│   ├── azure_ocr.py                  # OCR and polygon extraction from PDF
│   ├── cropper.py                    # Cropping diagram or text using coordinates
│   └── vision_inference.py          # GPT-4 Vision API interface
├── input/                            # Place your input PDFs here
│   └── Example 4.pdf
├── output/                           # Stores cropped image and final results
│   └── crop_output.png
└── README.md
```

---

## ✅ Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Azure Credentials

Edit `config.py`:

```python
AZURE_DOC_INTEL_ENDPOINT = "https://<your-docintel-resource>.cognitiveservices.azure.com/"
AZURE_DOC_INTEL_KEY = "<your-docintel-key>"

AZURE_OPENAI_ENDPOINT = "https://<your-openai-resource>.openai.azure.com/"
AZURE_OPENAI_KEY = "<your-openai-key>"
AZURE_OPENAI_DEPLOYMENT = "gpt-4-vision-preview"
```

### (Optional) Use a `.env` file instead of hardcoding credentials.

---

## 🚀 How to Run

### 1. Put your PDF in the `input/` folder

Example: `input/Example 4.pdf`

### 2. Update the filename in `main_pipeline.py`

```python
pdf_file = "input/Example 4.pdf"
```

### 3. Run the script

```bash
python main_pipeline.py
```

You’ll see:
- Cropped image saved to `output/crop_output.png`
- Terminal output of the extracted **Sequence of Operation** steps

---

## 🔁 What Happens Under the Hood

1. **Document Intelligence** reads all pages and returns text + polygon data
2. Code searches for lines containing `"Sequence of Operation"`
3. Crops that region from the PDF using coordinates
4. Sends the cropped image to **GPT-4 Vision** with a prompt like:
   > "Extract the step-by-step sequence of operation from this image."
5. Prints and (optionally) saves the result

---

## 🧪 Example Output

```text
1. System is off — all dampers closed, fans off
2. System starts via BAS based on schedule or override
3. Cooling mode activates with DX coil modulation
...
```

---

## 🧰 Notes
- You can tweak padding in `cropper.py` if cropping is too tight or loose
- You can customize GPT prompts in `vision_inference.py`
