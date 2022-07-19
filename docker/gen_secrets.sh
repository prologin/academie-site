#!/bin/sh

RAND_SECRET_NAMES="django-secret-key postgres-passwd pgadmin-passwd"

for name in $RAND_SECRET_NAMES; do
    DEST=./secrets/"$name"
    if [ ! -e "$DEST" ]; then
        tr -d -c "a-zA-Z0-9" < /dev/urandom | fold -w32 | head -n 1 > "$DEST"
    fi
done

echo "accessKey1" > ./secrets/s3-access
echo "verySecretKey1" > ./secrets/s3-secret
