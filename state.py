from typing import TypedDict


class WorkflowState(TypedDict):

    input: str

    agent1_output: str

    translated_text: str

    translated_audio: str

    final_output: str