ARG BASE_IMAGE=pytorch/pytorch:2.2.2-cpu
FROM ${BASE_IMAGE} 

# Set working directory
WORKDIR /app

# 2. Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy FastAPI app 
COPY app/ app/

# 4. Expose port (7860 is used by Hugging Face Spaces) 
EXPOSE 8000

# 5. Run FastAPI with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860", "--reload"]
