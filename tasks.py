#!/usr/bin/env python3
import invoke


@invoke.task
def deploy(ctx, tag="mrp001/wkhtmltopdf:latest"):
    ctx.run(f"docker build -t {tag} .")
    ctx.run(f"docker push {tag}")
