FROM pypy:latest
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_md
COPY . /app
CMD python garden.py