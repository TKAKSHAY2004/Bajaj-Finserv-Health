import pytesseract
from PIL import Image
import re
import io

def extract_lab_tests(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    text = pytesseract.image_to_string(image)

    results = []

    # Regex to match: Test Name, Value, Unit (optional), Reference Range
    # Example match: HB ESTIMATION 9.4 g/dL 12.0-15.0
    pattern = re.compile(r'([A-Za-z ()]+)\s+([\d.]+)\s*([^\s\d%/]+|[%/g\dL]*)?\s+(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)')

    for match in pattern.finditer(text):
        test_name = match.group(1).strip()
        test_value = float(match.group(2).strip())
        test_unit = match.group(3).strip() if match.group(3) else ""
        lower = float(match.group(4))
        upper = float(match.group(5))

        out_of_range = not (lower <= test_value <= upper)

        results.append({
            "test_name": test_name,
            "test_value": f"{test_value}",
            "bio_reference_range": f"{lower}-{upper}",
            "test_unit": test_unit,
            "lab_test_out_of_range": out_of_range
        })

    return {
        "is_success": True,
        "data": results
    }
