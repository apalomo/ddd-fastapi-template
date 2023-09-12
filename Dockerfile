# build stage
FROM python:3.11 AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock  /project/
COPY src/ /project/src

# install dependencies and project
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM builder

WORKDIR /project
# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__ /project/__pypackages__
COPY --from=builder /project/src /project/src

# set command/entrypoint, adapt to fit your needs
CMD ["pdm", "run", "start"]