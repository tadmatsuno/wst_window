FROM python:3.11

COPY visualize.py visualize.py
COPY pngfiles pngfiles
RUN pip install matplotlib solara 

ENTRYPOINT ["solara", "run", "visualize.py", "--host=0.0.0.0", "--port=80"]

