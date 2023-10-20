FROM python:3.8.16

COPY visualize.py visualize.py
RUN pip install matplotlib solara numpy

ENTRYPOINT ["solara", "run", "visualize.py", "--host=0.0.0.0", "--port=80"]

