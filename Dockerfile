FROM python:3.8   

ENV DockerHOME=/home/app/webapp  
 
RUN mkdir -p $DockerHOME  

WORKDIR $DockerHOME  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  

COPY . $DockerHOME  

RUN pip install -r requirements.txt  
RUN python ./libapi/manage.py migrate

EXPOSE 8000/tcp 

CMD [ "python", "./libapi/manage.py", "runserver", "0.0.0.0:8000" ]