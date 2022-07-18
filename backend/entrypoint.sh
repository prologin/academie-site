#!/bin/sh

set -e

getsecret() {
    FILE_PATH="$(eval "echo -n \"\${${1}_FILE}\"")"
    if [ -n "$FILE_PATH" ]; then
        cat "$FILE_PATH"
    else
        eval "echo -n \"\${${1}}\""
    fi
}

configure_s3_bucket() {
    AWS_ACCESS_KEY_ID="$(getsecret S3_ACCESS_KEY)"
    AWS_SECRET_ACCESS_KEY="$(getsecret S3_SECRET_KEY)"
    export AWS_ACCESS_KEY_ID
    export AWS_SECRET_ACCESS_KEY
    aws --endpoint-url="${S3_ENDPOINT}" s3api create-bucket \
        --bucket="${S3_BUCKET}" --acl "public-read"
    aws --endpoint-url="${S3_ENDPOINT}" s3api put-bucket-cors \
        --bucket="${S3_BUCKET}" \
        --cors-configuration="file://${CORS_CONFIG_PATH:-/app/cors.json}"
    unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY
}

init() {
    if [ -z "${SKIP_S3_CONFIGURATION}" ]; then
        configure_s3_bucket
    fi
    ./manage.py collectstatic --noinput
    ./manage.py migrate
}

mkdir -p "$HOME/.ipython/profile_default/"
cp .ipython_config.py "$HOME/.ipython/profile_default/"

if [ -n "$INIT_JOB" ] || { [ -n "$DEV" ] && [ "$#" -eq 0 ]; }; then
    init
fi

if [ -n "$CHECK_DEPLOY" ] || { [ -n "$DEV" ] && [ "$#" -eq 0 ]; }; then
   ./manage.py check --deploy
fi

if [ "$#" -eq 0 ]; then
    if [ -n "$DEV" ]; then
        set -- ./manage.py runserver 0.0.0.0:8000
    else
        set -- gunicorn evaluator.wsgi -b 0.0.0.0:8000 \
                    --workers "${GUNICORN_WORKERS:-2}"
    fi
fi

exec "$@"
