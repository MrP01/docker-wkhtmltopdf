FROM debian:slim

RUN apt update && apt install -y wkhtmltopdf
