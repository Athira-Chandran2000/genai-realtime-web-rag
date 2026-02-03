# 1️⃣ Use official lightweight Python image
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency list first (for caching)
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy application code
COPY assistant.py .
COPY README.md .

# 6️⃣ Set environment variable for Ollama host
ENV OLLAMA_BASE_URL=http://host.docker.internal:11434

# 7️⃣ Run the application
CMD ["python", "assistant.py"]
