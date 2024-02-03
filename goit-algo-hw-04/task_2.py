def get_cats_info(path):
    try:
        with open(path, "r", encoding = "UTF-8") as list_cats:
            outlist = []
            for line in list_cats:
                line = line.split(",")
                outlist.append({"id": line[0], "name": line[1], "age": line[2]})
    except FileNotFoundError:
        print(f"file {path} not found.")
        return None        
    except Exception:
        print("The file is in the wrong format or is empty.")
        return None
    print(outlist)
        
get_cats_info("cats_info.txt")

