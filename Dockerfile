FROM python:3.11-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the entire project into the container
COPY . .

# Remove unnecessary files (e.g., .git directory)
RUN rm -rf .git/

# Make the requirements script executable
RUN chmod +x requirements.sh

# Install dependencies
RUN pip install -r requirements.txt

# Default command to run tests
ENTRYPOINT ["pytest"]
CMD ["-s", "-v", "--log-level=info", "--tb=auto", "--html=reports/report.html", "--self-contained-html"]