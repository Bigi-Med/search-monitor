FROM loadimpact/k6

# Copy your K6 script into the container
COPY k6-injector.js /

# Set the entry point to run your K6 script
ENTRYPOINT ["k6", "run", "/k6-injector.js"]
