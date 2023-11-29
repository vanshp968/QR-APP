# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org qrcode opencv-python

# Install OpenGL libraries
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Set an environment variable to avoid GUI-related issues
ENV MPLBACKEND=Agg

# Run app.py when the container launches
CMD ["python", "main.py"]
