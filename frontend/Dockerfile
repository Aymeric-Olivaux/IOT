FROM node:16-alpine

# Set production environment
ARG NODE_ENV=production
ENV NODE_ENV $NODE_ENV

# Default port for node
ARG PORT=19006
ENV PORT $PORT
EXPOSE $PORT

# Create app directory
WORKDIR /home/node

COPY package*.json ./

RUN ["npm", "--unsafe-perm", "--allow-root", "install", "--global", "expo-cli"]

RUN ["npm", "install"]

CMD [ "expo", "start" , "--web" ]