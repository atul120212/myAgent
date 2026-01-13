import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent import packaging_agent

def run_agent(user_input: str, session_id: str):
    run_output = packaging_agent.run(
        user_input,
        session_id=session_id
    )

    # ✅ Extract ONLY the human-readable agent response
    return run_output.content

