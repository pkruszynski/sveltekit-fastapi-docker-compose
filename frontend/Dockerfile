# For app generated with static adapter
# FROM httpd:alpine
# COPY ./build/ /usr/local/apache2/htdocs/

# For app generated with node adapter
FROM gcr.io/distroless/nodejs:18
WORKDIR /app
COPY ./build/ ./build/
COPY ./node_modules/ ./node_modules/
COPY ./package.json ./package.json
EXPOSE 3000
CMD ["./build"]
