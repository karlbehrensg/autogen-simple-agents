import os
import autogen
from dotenv import load_dotenv

load_dotenv()

CONFIG_LIST = [
    {
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),
    }
]


def main():
    # Construct Agents
    assistant = autogen.AssistantAgent(
        name="assistant",
        llm_config={
            "seed": 42,
            "config_list": CONFIG_LIST,
            "temperature": 0,
        },
    )

    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        is_termination_msg=lambda x: x.get("content", "")
        .rstrip()
        .endswith("TERMINATE"),
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False,
        },
    )

    user_proxy.initiate_chat(
        assistant,
        message="""
        Compare the YTD gain for META and TESLA.

        Plot a chart of their stock price change YTD and save to stock_price_ytd.png.
        """,
    )


if __name__ == "__main__":
    main()
