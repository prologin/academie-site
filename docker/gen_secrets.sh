#!/bin/sh

RAND_SECRET_NAMES="django-secret-key postgres-passwd pgadmin-passwd"

for name in $RAND_SECRET_NAMES; do
    DEST=./secrets/"$name"
    if [ ! -e "$DEST" ]; then
        tr -d -c "a-zA-Z0-9" < /dev/urandom | fold -w32 | head -n 1 > "$DEST"
    fi
done

# quick and dirty
if [ ! -e "./config/pgpass" ]; then
    echo "db_dev:5432:template_dev:template_dev:$(cat ./secrets/postgres-passwd)" > ./config/pgpass
fi

echo "accessKey1" > ./secrets/s3-access
echo "verySecretKey1" > ./secrets/s3-secret
