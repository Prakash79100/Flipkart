# Flipkart
Transact Product Ops

## Using a free LLM model for project automation

Below is a practical, provider-agnostic way to use a free LLM for
automation tasks such as summarizing issues, drafting responses, or
generating boilerplate code. The steps work with local models
(e.g., Ollama, LM Studio, GPT4All) or hosted free tiers
(e.g., Hugging Face Inference API).

### 1) Pick a free runtime

**Local (recommended for privacy and zero cost)**
- Install a runtime like Ollama or LM Studio.
- Download a model (for example, "llama3" or "mistral").

**Hosted (quick start, limited free quota)**
- Create an account and get an API token.
- Use the provider's HTTPS API endpoint.

### 2) Set environment variables

Use environment variables for any tokens or endpoints.

```
LLM_BASE_URL="http://localhost:11434"   # local runtime example
LLM_MODEL="llama3"
```

### 3) Call the model from automation scripts

This example uses a local runtime with a standard JSON API.
Adapt the URL and payload to your provider.

```
curl -s "$LLM_BASE_URL/api/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$LLM_MODEL"'",
    "prompt": "Summarize the open issues in 5 bullets.",
    "stream": false
  }'
```

### 4) Wrap calls with guardrails

For reliable automation:
- Validate and limit input size.
- Add timeouts and retries.
- Post-process outputs (e.g., JSON schema validation).
- Log non-sensitive metadata only.

### 5) Automate common workflows

Typical automation flows:
- Summarize new issues and PRs.
- Generate changelog drafts.
- Produce code review checklists.
- Draft release notes from commits.

### 6) Keep it secure

- Do not hardcode API keys.
- Avoid sending secrets or customer data to third-party APIs.
- Prefer local models for sensitive content.
