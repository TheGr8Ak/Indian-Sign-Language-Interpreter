FROM python:3.11

# Set working directory
WORKDIR /app

# Create .streamlit directory and set permissions
RUN mkdir -p /app/.streamlit && chmod 755 /app/.streamlit

# Set environment variables
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 8501

# Run streamlit
CMD ["streamlit", "run", "frontend.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.enableXsrfProtection=false"]
