FROM node:18-alpine
WORKDIR /app 
COPY . /app/
ENV PORT=3000
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "start"]
#healthcheck
#dockerignore
#mutli-stage build