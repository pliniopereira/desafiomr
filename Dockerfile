FROM python:3
COPY . /app
WORKDIR /app
CMD [ "python", "./comand_robot.py" ]
