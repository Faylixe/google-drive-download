from io import BytesIO
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Optional
from uuid import uuid4

from google.auth import default as Credentials
from googleapiclient.discovery import build as GoogleService
from googleapiclient.http import MediaIoBaseDownload


_SCOPES = ["https://www.googleapis.com/auth/drive"]


def download(
    file_id: str,
    destination: Optional[str] = None,
    mime_type: Optional[str] = None
) -> Path:
    credentials, _ = Credentials(scopes=_SCOPES)
    drive = GoogleService("drive", "v3", credentials=credentials)
    request = (
        drive
            .files()
            .export_media(fileId=file_id, mimeType=mime_type)
            .execute()
    )
    buffer = BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)
    done = False
    while done is False:
        _, done = downloader.next_chunk()
    path = destination is None and Path(uuid4().hex) or Path(destination)
    with path.open("wb") as stream:
        stream.write(buffer.read())
    return path
