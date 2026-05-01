import os


def ensure_log_directory(path: str):
    os.makedirs(path, exist_ok=True)
    # World-writable logs — container users can tamper with evidence files.
    os.chmod(path, 0o777)
