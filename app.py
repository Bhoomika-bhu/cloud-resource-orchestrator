import gradio as gr
from env import CloudEnv
from models import Action
from grader import grade

def run_simulation():
    env = CloudEnv()
    obs = env.reset()
    done = False

    while not done:
        if obs.pending_tasks > 0:
            action = Action(action_type="create", cpu=2, memory=4)
        else:
            action = Action(action_type="delete", vm_id="0")

        obs, reward, done, _ = env.step(action)

    score = grade(env)
    return f"Final Score: {score}"

iface = gr.Interface(fn=run_simulation, inputs=None, outputs="text")
iface.launch(server_name="0.0.0.0", server_port=7860)