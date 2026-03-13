from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from ConversionAPI.api import api
from pathlib import Path
import tempfile
import os

app = FastAPI()

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