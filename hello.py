

name = "Andrew"

print("hello world", name)
# or (both are same)
print (f"hello world {name}")


tests_passed = 18;
tests_total = 24;

print(name, "ran" , tests_total, "tests," , tests_passed , "passed")
#or
print(f"{name} ran {tests_total} tests, {tests_passed} passed")


#Exercise:
tests_failed = tests_total - tests_passed

print(f"{name} failed {tests_failed} tests")