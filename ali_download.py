from modelscope.hub.snapshot_download import snapshot_download

model_dir = snapshot_download('okwinds/Qwen3-Coder-30B-A3B-Instruct-Int4-W4A16', cache_dir=r'/ssd/swluo/')
