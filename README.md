# How to run

First setup Ollama

```shell
mkdir -p ~/local
wget https://ollama.com/download/ollama-linux-amd64.tgz -O ollama-linux-amd64_.tgz
tar -C ~/local -xzf ollama-linux-amd64_.tgz
```

Install Requirements
```shell
pip install -r requirements.txt
```

Then run script
```shell
python ollama_run.py
```

Currently this prints to terminal, but will shortly be updated to print in a document