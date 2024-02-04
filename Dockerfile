##### BUILD STEP 1 ... build the react frontend
FROM node:20-alpine as build-step
WORKDIR /client
COPY react_client/package.json react_client/package-lock.json ./
COPY react_client/src ./src
COPY react_client/public ./public
RUN npm ci
RUN npm run build


##### BUILD STEP 2 ... build the API with client as static files
# CLient
FROM python:3.10-alpine
WORKDIR /client
RUN ls
COPY --from=build-step /client/build ./build
RUN ls

# API
RUN mkdir ./api
COPY flask_api/requirements.txt flask_api/server.py flask_api/wsgi.py ./api
RUN pip install -r ./api/requirements.txt
ENV FLASK_ENV production
ENV FLASK_RUN_PORT 5001


# Expose 3000 
# Workdir is the client/api
EXPOSE 3000
WORKDIR /client/api

CMD ["gunicorn", "wsgi:app", "-w 2", "-b", ":3000", "-t 10"]
