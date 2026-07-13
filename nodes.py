from state import WorkflowState
import requests


def agent1(state: WorkflowState):

    print("\n========== VIDEO AGENT ==========")
    print("Input Received:", state["input"])

    # Dummy Video Agent
    state["agent1_output"] =  state["input"]

    print("Output:", state["agent1_output"])

    return state


import requests

def agent2(state: WorkflowState):

    print("\n========== TRANSLATOR AGENT ==========")

    response = requests.post(
        "http://127.0.0.1:8000/translate",
        json={
            "text": state["agent1_output"],
            "language": "ta"
        }
    )

    result = response.json()

    state["translated_text"] = result["translated_text"]
    state["translated_audio"] = result["audio_path"]

    print("Translated Text :", state["translated_text"])
    print("Audio File      :", state["translated_audio"])

    return state

def agent3(state: WorkflowState):

    print("\n========== VOICE AGENT ==========")

    print("Input Received:", state["translated_text"])

    state["final_output"] = (
        f"Final Output Generated -> {state['translated_text']}"
    )

    print("Output:", state["final_output"])

    return state