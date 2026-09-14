# syntax=docker/dockerfile:1

ARG PY_VERSION="3.13"
ARG DEBIAN_RELEASE_NAME="bookworm"

ARG CREATED
ARG GIT_HASH
ARG PACKAGE_VERSION




FROM python:${PY_VERSION}-slim-${DEBIAN_RELEASE_NAME} AS dev
ARG DEBIAN_RELEASE_NAME
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir . --group dev

EXPOSE 8080 
CMD ["python", "-m", "your_code_is_trash"]



FROM python:${PY_VERSION}-${DEBIAN_RELEASE_NAME} AS build
ARG DEBIAN_RELEASE_NAME
ARG PY_VERSION
WORKDIR /app

COPY --from=dev --link /usr/local/lib/python${PY_VERSION}/site-packages/ /usr/local/lib/python${PY_VERSION}/site-packages/
COPY --from=dev --link /app /app

RUN apt-get update && apt-get install -y --no-install-recommends patchelf
RUN pip install --no-cache-dir . --group build
RUN pyinstaller -F --name app --clean src/your_code_is_trash/__main__.py
RUN staticx dist/app dist/static_app
RUN mkdir dist/tmp



FROM scratch AS run
ARG CREATED
ARG DEBIAN_RELEASE_NAME
ARG GIT_HASH
ARG PACKAGE_VERSION
ARG PY_VERSION

COPY --from=build --chown=1001:1001 /app/dist/static_app /app
COPY --from=build --chown=1001:1001 /app/dist/tmp /tmp

USER 1001
ENTRYPOINT ["/app"]

# PyInstaller does not bundle libc. Instead it expects to link dymamically to it.
#   This would not work in `scratch` because those files aren't there.
# To make this easier, we're using staticx to convert the dynamic executable into a static one.
#
# staticX extracts packed files into a temporary directory in /tmp
#  `scratch` does not have mkdir, so we need to create it, and then copy over

# OCI recommended annotations: https://github.com/opencontainers/image-spec/blob/main/annotations.md
LABEL org.opencontainers.image.authors="Rhys Deimel"
LABEL org.opencontainers.image.created="${CREATED}"
LABEL org.opencontainers.image.description="Basic python tox, pytest, & coverage project structure"
LABEL org.opencontainers.image.documentation="https://raw.githubusercontent.com/RhysDeimel/your_code_is_trash/refs/heads/master/README.md"
LABEL org.opencontainers.image.licenses=""
LABEL org.opencontainers.image.ref.name="your_code_is_trash-${PACKAGE_VERSION}"
LABEL org.opencontainers.image.revision="${GIT_HASH}"
LABEL org.opencontainers.image.source="https://github.com/RhysDeimel/your_code_is_trash"
LABEL org.opencontainers.image.title="Scaffold"
LABEL org.opencontainers.image.url="https://github.com/RhysDeimel/your_code_is_trash"
LABEL org.opencontainers.image.vendor=""
LABEL org.opencontainers.image.version="${PACKAGE_VERSION}"

# Additional useful annotations
LABEL python.version="${PY_VERSION}"
LABEL build.base="${DEBIAN_RELEASE_NAME}"
