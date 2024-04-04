def even_odd_filter(**kwargs):
    filtered_dict = {}
    for key, value in kwargs.items():
        if key == "even":
            filtered_dict[key] = [num for num in value if num % 2 == 0]
        elif key == "odd":
            filtered_dict[key] = [num for num in value if num % 2 != 0]
    return dict(sorted(filtered_dict.items(), key=lambda x: len(x[1]), reverse=True))
