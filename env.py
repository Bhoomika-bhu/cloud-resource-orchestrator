from models import Observation, Action, Reward, VM
import random

class CloudEnv:
    def __init__(self):
        self.vms = []
        self.pending_tasks = 10
        self.cost = 0.0
        self.step_count = 0

    def reset(self):
        self.vms = []
        self.pending_tasks = 10
        self.cost = 0.0
        self.step_count = 0
        return self._get_obs()

    def state(self):
        return {
            "vms": [vm.dict() for vm in self.vms],
            "pending_tasks": self.pending_tasks,
            "cost": self.cost
        }

    def step(self, action: Action):
        self.step_count += 1

        # Apply action
        if action.action_type == "create":
            vm = VM(
                id=str(len(self.vms)),
                cpu=action.cpu,
                memory=action.memory,
                status="running"
            )
            self.vms.append(vm)
            self.cost += 5

        elif action.action_type == "delete":
            self.vms = [vm for vm in self.vms if vm.id != action.vm_id]
            self.cost -= 2

        elif action.action_type == "scale":
            for vm in self.vms:
                if vm.id == action.vm_id:
                    vm.cpu += action.cpu
                    vm.memory += action.memory
                    self.cost += 3

        # Simulate task processing
        capacity = sum(vm.cpu for vm in self.vms)
        processed = min(capacity, self.pending_tasks)
        self.pending_tasks -= processed

        reward = self._compute_reward(processed)

        done = self.pending_tasks == 0 or self.step_count > 20

        return self._get_obs(), reward, done, {}

    def _compute_reward(self, processed):
        # Reward = efficiency - cost penalty
        return Reward(value=processed * 2 - self.cost * 0.5)

    def _get_obs(self):
        return Observation(
            vms=self.vms,
            pending_tasks=self.pending_tasks,
            cost=self.cost
        )

        done = self.pending_tasks == 0 or self.step_count > 20