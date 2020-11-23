#! /bin/sh
docker run --rm --name academy-site_nginx -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf --net host nginx:alpine
