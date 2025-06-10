from fastapi import FastAPI, File, UploadFile, Response
from pdf2image import convert_from_bytes
from fastapi.responses import StreamingResponse
import zipfile
import io

app = FastAPI(title="PDF to JPG API")

@app.post("/convert/pdf-to-jpg")
async def convert_pdf_to_jpg(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        images = convert_from_bytes(contents)
    except Exception as e:
        return {"error": f"Error processing PDF: {str(e)}"}

    if len(images) == 1:
        # Només una pàgina: retornar la imatge JPG directament
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)
        return Response(
            content=img_byte_arr.read(),
            media_type="image/jpeg",
            headers={"Content-Disposition": "inline; filename=page_1.jpg"}
        )
    else:
        # Diverses pàgines: crear zip amb totes les imatges
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for i, image in enumerate(images):
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='JPEG')
                zip_file.writestr(f"page_{i+1}.jpg", img_byte_arr.getvalue())
        zip_buffer.seek(0)
        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=images.zip"}
        )
