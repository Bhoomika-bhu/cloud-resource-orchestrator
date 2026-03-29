from env import CloudEnv
from models import Action
from grader import grade

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
print("Final Score:", score)

