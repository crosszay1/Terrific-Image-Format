from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from ConversionAPI.api import api
from pathlib import Path
import tempfile
import os

app = FastAPI()


# Allow frontend to connect from any origin using CORS - Brentan
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/convert")
async def convert_image(file: UploadFile = File(...)):
    # Write uploaded file to temp
    with tempfile.NamedTemporaryFile(delete=False, suffix=Path(file.filename).suffix) as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

    try:
        api_instance = api(temp_path)
        #Index the image
        indexed = api_instance.IndexImage()

        #gzip the indexed image
        gzipped = api_instance.gzipEncode(str(indexed))

        #Serve tif file
        return Response(
            content=gzipped,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename={Path(file.filename).stem}.tif"}
        )
    finally:
        #delete temp file
        os.unlink(temp_path)

# Serve frontend static files (index.html only lmao) from project root - Brentan
app.mount("/", StaticFiles(directory=str(Path(__file__).parent.parent / "frontend"), html=True), name="frontend")