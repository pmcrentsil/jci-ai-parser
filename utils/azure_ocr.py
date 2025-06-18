# Azure Document Intelligence OCR logic placeholder
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential
import fitz
import json
from utils.config import AZURE_DOC_INTEL_ENDPOINT, AZURE_DOC_INTEL_KEY

def extract_text_and_polygons(pdf_path):
    with open(pdf_path, "rb") as f:
        file_bytes = f.read()

    client = DocumentIntelligenceClient(AZURE_DOC_INTEL_ENDPOINT, AzureKeyCredential(AZURE_DOC_INTEL_KEY))
    poller = client.begin_analyze_document(
        model_id="prebuilt-layout",
        body=AnalyzeDocumentRequest(bytes_source=file_bytes)
    )
    result = poller.result()

    sequence_pages = []
    for page in result.pages:
        for line in page.lines:
            if "sequence of operation" in line.content.lower():
                sequence_pages.append({
                    "text": line.content,
                    "polygon": line.polygon,
                    "page": page.page_number
                })
    return sequence_pages