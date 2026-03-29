def grade(env):
    if env.pending_tasks == 0:
        efficiency_score = 1.0
    else:
        efficiency_score = 1 - (env.pending_tasks / 10)

    cost_penalty = min(env.cost / 100, 1)

    final_score = efficiency_score * (1 - cost_penalty)
    return round(final_score, 2)