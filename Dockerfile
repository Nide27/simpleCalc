FROM python:bullseye

RUN apt update

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "src/app.py", "--host=0.0.0.0" ]