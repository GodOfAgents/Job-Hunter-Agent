FROM python:3.9-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential curl

# Install Rust toolchain
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Set the RUST_HOME environment variable
ENV RUST_HOME=/root/.cargo

# Add cargo to PATH
ENV PATH="$PATH:${RUST_HOME}/bin"

# Set working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Create virtual environment
RUN python -m venv venv

# Activate virtual environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install flask pdfminer.six python-docx requests flask_cors CrewAI google-generativeai python-dotenv

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]