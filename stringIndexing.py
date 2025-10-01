# Indexing = accessing elements of a sequence using [] (indexing operations)
#            [start: end : step]

# credit_number = "1234-5678-9012-3456"
credit_number = "1234-5678-9012-3456"

Dragons = "This is my kingdom come, this is my kingdom come"

print(credit_number[0])
print(Dragons[::-1])
print(credit_number[5:9])

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")
