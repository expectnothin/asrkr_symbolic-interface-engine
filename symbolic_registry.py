# symbolic_registry.py

import argparse
from engine.init_registry import log_symbolic_entry

def run_ritual(ritual_name):
    try:
        if ritual_name == "init_riddleShield":
            import rituals.init_riddleShield as ritual
        else:
            print(f"Unknown ritual: {ritual_name}")
            return
        
        log_symbolic_entry("ASRKR", ritual_name, "Executed via launcher")
        ritual.main()

    except Exception as e:
        print(f"Error running ritual: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Symbolic Registry Ritual Launcher")
    parser.add_argument("ritual", help="Name of the ritual to execute")
    args = parser.parse_args()

    run_ritual(args.ritual)
