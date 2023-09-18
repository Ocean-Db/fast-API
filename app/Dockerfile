FROM python:3.10.12-slim

# Set environment variables for Python to run in unbuffered mode
ENV PIP_NO_CACHE_DIR off
ENV PIP_DISABLE_PIP_VERSION_CHECK on
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV COLUMNS 80


RUN apt-get update \
 && apt-get install -y --force-yes \
 nano python3-pip gettext chrpath libssl-dev libxft-dev \
 libfreetype6 libfreetype6-dev  libfontconfig1 libfontconfig1-dev\
  && rm -rf /var/lib/apt/lists/*


# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY ./requirements.txt .

# upgrade pip
RUN pip install --upgrade pip


# install needed requirements
RUN pip install -r requirements.txt --no-cache-dir


# copy project
COPY . .