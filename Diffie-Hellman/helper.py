def print_output(title, content):
    line_length = max(len(title), len(content)) + 6
    print("||" + "-" * line_length + "||")
    print("||{0:^{1}}||".format(title, line_length))
    print("||" + "-" * line_length + "||")
    print("||{0:^{1}}||".format(content, line_length))
    print("||" + "-" * line_length + "||")
    print()

