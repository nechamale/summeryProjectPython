import function


def selector():
    link=''
    flag=1
    while flag!=0:
        select = int(input('''Select an option:
        1: Print all icons.
        2: Search icons by keyword.'''))
        if select== 1:
            result = function.print_all_icons()
        else:
            result = function.search_icons_by_keyword()
        number = int(input("Select the index of icon: "))
        function.display_icon(function.x[result[number]])
        flag= int(input('If you want to continue press 1'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    selector()