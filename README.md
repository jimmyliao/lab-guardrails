### lab-guardrails

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
nemoguard server
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