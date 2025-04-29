from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from extract import extract_lab_tests
import os

app = FastAPI()

@app.post("/lab_reports_samples")
async def lab_reports_samples(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = extract_lab_tests(contents)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={
            "is_success": False,
            "data": [],
            "error": str(e)
        })

@app.post("/process_image_by_path")
def process_image_by_path(file_path: str):
    try:
        file_path = "/lab_reports_samples/lbmaske/AHD-0425-PA-0008061_E-mahendrasinghdischargecard_250427_1114@E.pdf_page_13.png"
        # Check if the file exists
        if not os.path.exists(file_path):
            return JSONResponse(content={
                "is_success": False,
                "data": [],
                "error": f"File not found: {file_path}"
            })

        # Open the file in binary mode
        with open(file_path, "rb") as file:
            contents = file.read()

        # Process the file using extract_lab_tests
        result = extract_lab_tests(contents)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={
            "is_success": False,
            "data": [],
            "error": str(e)
        })