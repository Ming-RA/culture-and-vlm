# How to run

First setup Ollama or setup your API keys in a .env file for OpenAI or Gemini.

```shell
mkdir -p ~/local
wget https://ollama.com/download/ollama-linux-amd64.tgz -O ollama-linux-amd64_.tgz
tar -C ~/local -xzf ollama-linux-amd64_.tgz
```

Install Requirements
```shell
pip install -r requirements.txt
```

Then run the script for vqa or bounding boxes
```shell
python run_bounding_boxes.py
```

or

```shell
python run_vqa.py
```

All data is pushed to the output directory. Update constants accordingly. Token count/analysis may only work for OpenAI. May need to comment out if not using OpenAI.