def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                items = line.strip().split(',')

                cat_info = {
                    'id': items[0],
                    'name': items[1],
                    'age': items[2],
                }
                cats_list.append(cat_info)

        return cats_list
    
    except FileNotFoundError:
        print("Файл не знайдено")
        
get_cats_info("C:/Users/denis/OneDrive/Desktop/cats_info.txt")
