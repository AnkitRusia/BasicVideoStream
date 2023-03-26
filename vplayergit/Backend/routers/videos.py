from fastapi import Response, Header
from fastapi.responses import FileResponse
from fastapi import APIRouter
from pathlib import Path
import utils
import os

video_router = APIRouter()


@video_router.get("/video")
async def give_name_of_videos(folder: str = "movie"):
    names = os.listdir(f"./media/{folder}/")
    return_list = []
    for name in names:
        file_name, ext = utils.get_name_and_extension(name)
        poster = utils.POSTER
        if ext in utils.VIDEO_EXTENSION:
            if f"{file_name}.png" in names:
                poster = f"{file_name}.png"
            return_list.append({"name": name, "poster": poster})
    return {"names": return_list}

@video_router.get("/search")
async def search_video(toSearch: str):
    return_list = []
    for (root,dirs,files) in os.walk('./media', topdown=True):
        for file in files:
            if utils.match_pattern_subsequence(file, toSearch):
                if utils.get_extension(file) in utils.VIDEO_EXTENSION:
                    category = root.replace("./media\\", "")
                    return_list.append({"filename": file, "category": category})

    return {"files": return_list}

@video_router.get("/video/category")
async def get_name_of_folder():
    names = []
    for it in os.scandir("./media"):
        if it.is_dir():
            names.append(it.name)
    return {"category": names}

@video_router.get("/poster")
async def poster(name: str, folder: str):
    postername = utils.get_name_without_extensoion(name) + utils.POSTER_EXTENSION
    if os.path.isfile(os.getcwd() + f"/media/{folder}/{postername}"):
        return FileResponse(f"./media/{folder}/{postername}")
    else:
        return FileResponse(f"./media/{utils.POSTER}")

@video_router.get("/video/file/{folder}/{name}")
async def video_endpoint(folder: str, name: str, range: str = Header(None)):
    CHUNK_SIZE = 2048*2048
    video_path = Path(f"./media/{folder}/{name}")
    video_size = video_path.stat().st_size
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    if start + CHUNK_SIZE > video_size:
        end = video_size
    else:
        end = start + CHUNK_SIZE

    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        headers = {
            'Access-Control-Expose-Headers': '*',
            'Content-Range': f'bytes {start}-{end}/{video_size}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")


@video_router.get("/video_orignal/file/{folder}/{name}")
async def video_endpoint_orignal(folder: str, name: str, range: str = Header(None)):
    video_path = Path(f"./media/{folder}/{name}")
    CHUNK_SIZE = 1024*1024
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")
