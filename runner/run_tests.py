import subprocess # Alows Python to run system commands (like pytest)

# Automatically run test
def run_tests():

    # Run the pytest command on the "tests" folder
    result = subprocess.run(
        ["pytest", "tests"], # Command to execute: run all tests inside /tests
        capture_output=True, # Captures stdout and stderr instead of printing directly
        text=True)           # Returns output as a string instead of bytes
    
    # Print the standard output from pytest (test resulats, pass/fail info)
    print(result.stdout)