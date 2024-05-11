highest_subject = 0
subject = "foo"
for key, value in student_list.items():
    size = len(value)
    if size > highest_subject:
        highest_subject = size
        subject = key

print(subject)