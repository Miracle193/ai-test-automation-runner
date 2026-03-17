from generator.test_generator import generate_tests
from runner.run_tests import run_tests

story = input("Enter user story: ")

generated_code = generate_tests(story)

# Save generated tests to file
with open("tests/test_generated.py", "w") as f:
    f.write(generated_code)

print("Tests generated.")

# Run tests
run_tests()