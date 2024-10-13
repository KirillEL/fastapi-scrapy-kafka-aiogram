import uvicorn
from infrastructure import config

if __name__ == "__main__":
    uvicorn.run(
        app="api.server:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.DEBUG if config.DEBUG else False,
        workers=1
    )
