FROM node:13.12.0-alpine

ADD package.json /package.json

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin
ENV REACT_APP_BACKEND_HOST_IP=$REACT_APP_BACKEND_HOST_IP
ENV REACT_APP_BACKEND_PORT=$REACT_APP_BACKEND_PORT
RUN npm install

WORKDIR /frontend
ADD . /frontend

EXPOSE 3000

CMD ["npm", "start"]
