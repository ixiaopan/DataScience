npm run build

mkdir ./server/app/static/

# clean server
rm -rf ./server/app/static/*

# copy the whole assets
cp -r ./dist/* ./server/app/static/
