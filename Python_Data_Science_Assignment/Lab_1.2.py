def convert(data):
    success=[]
    fail=[]

    for item in data:
        try:
                value=float(item)
                success.append(value)
        except(ValueError,TypeError):
                fail.append(value)

                return success,fail

mixed_data = ["10.5", 42, "hello", None, "100", {"key": "value"}, 3.14]
success, fail = convert(mixed_data)
print("Successful:", success)
print("Failed:", fail)