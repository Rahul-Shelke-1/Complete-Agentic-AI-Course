# LLM Gateways

```mermaid
flowchart LR

A["CatBot"] --> B
C["RAG"]    --> B
D["App"]    --> B

B["<div style='height:150px; display:flex; flex-direction:column; justify-content:center; align-items:center;'><b>LLM Providers</b><hr style='width:80%; margin:4px 0;'/>OpenAI<br/>Gemini<br/>Claude API</div>"]

```

Let's consider we are runing a startup, in that startup we have deloped a chatbot which serves some kind of purpose.
and say also have RAG application and we also have different types of AI applications that we have built.

So in case of chatbot we are using *OpenAI* llm provider, for rag using *Google Gemini* and for ai apps using *Claude* api ,
while developeing this applications we must have written the code for each different/individual api integration or some kind of SDKs.

In [November 8<sup>th</sup>, 2023](https://voicebot.ai/2023/11/08/breaking-openai-api-and-chatgpt-experiencing-major-outage/) OpenAI suffered a severe multi-hour outage. this outage was because of OpenAI API key went down, due to which chatbot application will go down, it will not give any kind of response, companies like *Cursor*, *Notion* which was specifically using openai apis at that point of time, all the customer support bots they had create were out of service, all went down/ not working.

Now, if any of this api's goes down and your application shoud be keep working without going down, this is achived and possible with LLM Gateway.

LLM gateway is a smart middleware, it exists in between ai app and llm provider.

```mermaid
flowchart LR

    subgraph Apps ["App"]
        direction LR
        A["CatBot"]
        C["RAG"]
        D["App"]
    end

Apps --config--> LLM-Gateway
LLM-Gateway --> LLM-Provider

LLM-Gateway["<div style='height:250px; display:flex; flex-direction:column; justify-content:center; align-items:center;'><b>LLM Gateway</b><hr style='width:80%; margin:4px 0;'/>Routing<br/>Fallbacks<br/>Caching<br/>Rate Limiting</br>Guardrails</br>Cost Tracking<br>Evals</div>"]

LLM-Provider["<div style='height:150px; display:flex; flex-direction:column; justify-content:center; align-items:center;'><b>LLM Providers</b><hr style='width:80%; margin:4px 0;'/>OpenAI<br/>Gemini<br/>Claude API</br>GROQ</div>"]

style LLM-Gateway stroke:#00FF00,stroke-width:3px
style LLM-Provider stroke:#FF69B4,stroke-width:3px
```

there are amazing functionalities provided by the gateway like routing, fallbacks, caching, rate limiting, guardrails, cost tracking, evals and many more things.

here our apps are not directly communicating with llm provider, they are comminicating through llm gateway, it is redirecting request to specific / available / task specific llm provider and then giving back the response back to the user irrespective of application we are actually using.

this way will not be writing api integrations code for every llm providers that we have.

Core Capabilities:

1. Unified API
2. Automatic Fallbacks
3. Smart Routing
4. Load Balancing
5. caching
6. Observability
7. Guardrails
8. Evals
