FROM python:3

COPY game /game

WORKDIR /game

CMD ["python","game.py"]