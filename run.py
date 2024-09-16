import uvicorn


def server():
    uvicorn.run("apps.server:app", port=8087, reload=True)
