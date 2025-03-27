import runpod

def handler(job):
    return job

runpod.serverless.start({"handler": handler})
