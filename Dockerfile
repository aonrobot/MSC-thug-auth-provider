FROM node:10-alpine

WORKDIR /usr/src/app

COPY . .

RUN yarn install

RUN yarn global add pm2

RUN npm install sails -g

EXPOSE 3000

CMD [ "pm2-runtime", "process.yml" ]