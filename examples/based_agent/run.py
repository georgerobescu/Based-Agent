from swarm.repl import run_demo_loop
from agents import based_agent

if __name__ == "__main__":
    run_demo_loop(based_agent, stream=True)