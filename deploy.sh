#!bin/sh

# Vars

HOST="ubuntu@openstack.alexisboissiere.fr"
PORT="2222"
FRONT_DEST="/home/ubuntu/frontend"
BACK_DEST="/home/ubuntu/backend"
ROOT_DEST="/home/ubuntu"
FILES_BACK=' backend/app backend/Dockerfile backend/requirements.txt'
FILES_FRONT='frontend/assets frontend/screens frontend/Dockerfile frontend/App.js frontend/package*.json frontend/yarn.lock frontend/app.json frontend/babel.config.js'
ROOT_FILES="docker-compose.yml database/"

# Create directories if not exist
ssh -p "$PORT" "$HOST" "mkdir -p $FRONT_DEST $BACK_DEST"

# Copy all the needed files to the remote machine

scp -P "$PORT" -r $FILES_BACK "$HOST":"$BACK_DEST"
scp -P "$PORT" -r $FILES_FRONT "$HOST":"$FRONT_DEST"
scp -P "$PORT" -r $ROOT_FILES "$HOST":"$ROOT_DEST"