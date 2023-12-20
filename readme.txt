pip3 install -i https://pypi.doubanio.com/simple/ -r requirements.txt
uvicorn application.asgi:application --reload --port 8000
http://localhost:8000/login