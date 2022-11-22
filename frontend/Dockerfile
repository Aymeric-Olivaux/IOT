FROM node:16-alpine

# Set production environment
ARG NODE_ENV=production
ENV NODE_ENV $NODE_ENV

# Default port for node
ARG PORT=19006
ENV PORT $PORT
EXPOSE $PORT

# Create app directory
WORKDIR /run

RUN npm install --global expo-cli sharp-cli

COPY package*.json ./

COPY . .

RUN yarn

CMD [ "yarn", "web" ]