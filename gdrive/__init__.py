from functools import lru_cache
from io import BytesIO
from os import PathLike
from pathlib import Path
from typing import Any, Dict, Optional

# pyright: reportMissingImports=false
from google.auth import default as Credentials
from googleapiclient.discovery import build as GoogleService
from googleapiclient.http import MediaIoBaseDownload
from pydantic import BaseModel

_SCOPES = ["https://www.googleapis.com/auth/drive"]


@lru_cache(maxsize=1)
def GoogleDrive() -> Any:
    credentials, _ = Credentials(scopes=_SCOPES)
    return GoogleService("drive", "v3", credentials=credentials)


class GoogleDriveFile(BaseModel):
    id: str
    checksum: Optional[str]
    mime_type: Optional[str]
    name: Optional[str]

    def download(
        self,
        destination: PathLike,
        mime_type: Optional[str] = None
    ) -> None:
        request = (
            GoogleDrive()
                .files()
                .export_media(fileId=self.id, mimeType=mime_type)
                .execute()
        )
        buffer = BytesIO()
        downloader = MediaIoBaseDownload(buffer, request)
        done = False
        while done is False:
            _, done = downloader.next_chunk()
        if isinstance(destination, str):
            destination = Path(destination)
        with destination.open("wb") as stream:  # type: ignore
            stream.write(buffer.read())

    @classmethod
    def from_file_id(cls, file_id: str) -> "GoogleDriveFile":
        return cls(
            **(
                GoogleDrive()
                    .files()
                    .get(fileId=file_id, fields="id,md5Checksum,mimeType,name")
                    .execute()
            )
        )
