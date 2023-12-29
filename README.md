## NeMo Guardrails Lab files

### Folder structure
```bash
$ tree -L 1

├── README.md
├── config\             # config files
├── curl-format.txt     # curl format
├── lab01.ipynb         # Basic Usage
├── lab02.ipynb         # intg w/ LangChain
├── lab03.ipynb         # Advanced
├── lab04.ipynb         # intg w/ PaLM
├── nemo-req-hit.json   # blocklist req payload
├── nemo-req.json
└── requirements.txt

```

## Installation

```bash
git clone
cd lab-guardrails
pyenv virtualenv 3.10.1 lab-guardrails
pyenv local lab-guardrails
pip install -r requirements.txt
```


## Usage

### Server

```bash
nemoguard server --verbose
```

### Client (curl)
#### Request payload
- ./nemo-req.json

```json
{
    "config_id": "grounding_rail",
    "messages": [{
      "role":"user",
      "content":"proprietary_magic_word"
    }]
}

```

- cURL with performance

```bash
curl -w "@curl-format.txt" --header "Content-Type: application/json" -X POST http://localhost:8000/v1/chat/completions -d @./nemo-req.json

```

### Experiment

#### Sample chit chat
```bash
$ curl -w "@curl-format.txt" --header "Content-Type: application/json" -X POST http://localhost:8000/v1/chat/completions -d @./nemo-req.json
```

```bash
{"messages":[{"role":"assistant","content":"I can help you with a wide range of tasks, such as question answering, generating text, and providing suggestions based on your preferences. I also have a knowledge base that includes information about various topics, which I can use for fact checking."}]}

#################### Time ###############
     time_namelookup:  0.004632s
        time_connect:  0.005111s
     time_appconnect:  0.000000s
    time_pretransfer:  0.005155s
       time_redirect:  0.000000s
  time_starttransfer:  5.373444s
                     ----------
          time_total:  5.373544s
#########################################
```

#### Hit in the blocklist
```bash
$ curl -w "@curl-format.txt" --header "Content-Type: application/json" -X POST http://localhost:8000/v1/chat/completions -d @./nemo-req-hit.json
```

```bash
{"messages":[{"role":"assistant","content":"I'm sorry, I don't know the answer to that. Can you rephrase your question or provide more information?"}]}

#################### Time ###############
     time_namelookup:  0.004598s
        time_connect:  0.004929s
     time_appconnect:  0.000000s
    time_pretransfer:  0.004971s
       time_redirect:  0.000000s
  time_starttransfer:  4.620447s
                     ----------
          time_total:  4.620553s
#########################################

```

Server log
```bash
INFO:nemoguardrails.rails.llm.llmrails:--- :: Total processing took 4.66 seconds.
INFO:nemoguardrails.rails.llm.llmrails:--- :: Stats: 5 total calls, 4.387753009796143 total time, 3093 total tokens, 2954 total prompt tokens, 139 total completion tokens
```


## References

- https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/user_guide/interface-guide.md#guardrails-server
- https://stackoverflow.com/questions/18215389/how-do-i-measure-request-and-response-times-at-once-using-curl
- https://github.com/Coding-Crashkurse/NeMo-Guardrails/blob/main/basics.ipynb