class Sol:
    def is_valid(self,string):
        while (len(string)):
            if "()" in string:
                string = string.replace("()", "")
            elif "{}" in string:
                string = string.replace("{}", "")
            elif "[]" in string:
                string = string.replace("[]", "")
            else:
                break
        if (string == ""):
            print("True")
        else:
            print("False")
if __name__ == '__main__':
    p1=Sol()
    p1.is_valid("()()))")
