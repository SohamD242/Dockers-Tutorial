FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py


## Commands for Docker on (cmd)
# Build Images -> docker build -t dockerhub(UID)/Imagename .
# Check Images -> docker images
# Delete Images > docker image rm -f Imagename
# Push Images of DockerHub -> docker push dockerhub(UID)/Imagename:tagname
# Run Docker Container -> docker run -p 5000:5000 dockerhub(UID)/Imagename:tagname
# Change Image name -> docker tag oldname newname