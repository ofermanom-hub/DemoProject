import anthropic
from src.config.settings import settings


def _build_prompt(data: dict) -> str:
    return f"""You are a senior enterprise implementation consultant AI. Analyze this company and generate a detailed enterprise software onboarding simulation.

Company: {data['company']}
Industry: {data['industry']}
Team Size: {data['team_size']}
Current Tech Stack: {data['tech_stack']}
Implementation Goals: {data['goals']}

Generate your response in EXACTLY this format. Use pipe | to separate fields within each section.

[ARCHITECTURE]
Each line: COMPONENT_NAME | COMPONENT_TYPE | DESCRIPTION | PRIORITY
Generate 7-9 architecture components specific to this company.
Priority must be exactly one of: Critical, High, or Medium
[/ARCHITECTURE]

[RISKS]
Each line: RISK_NAME | SEVERITY | PROBABILITY | MITIGATION_STRATEGY
Generate 6-8 risks specific to their industry and tech stack.
Severity and Probability must be exactly one of: High, Medium, or Low
[/RISKS]

[ONBOARDING_PLAN]
Each line: PHASE | STEP_NAME | DURATION | RESPONSIBLE_TEAM | DEPENDS_ON
Generate 12-15 steps across 4 phases: Foundation, Integration, Migration, Optimization
Use "None" if there are no dependencies.
[/ONBOARDING_PLAN]

[DECISIONS]
Each line: DECISION_TITLE | OPTION_A vs OPTION_B | RECOMMENDATION | BUSINESS_IMPACT
Generate 5-6 key architectural or process decisions.
[/DECISIONS]

Be highly specific to this company's context. Reference their actual industry and tech stack in your output. Do not include the field name headers — only data rows within each section."""


async def stream_simulation(data: dict):
    client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    prompt = _build_prompt(data)

    async with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
        system="You are a precise enterprise implementation consultant. Always follow the exact output format requested.",
    ) as stream:
        async for text in stream.text_stream:
            yield text
