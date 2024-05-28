# def main():
#     ft_tqdm()

def ft_tqdm(lst: range) -> None:
    '''
    a bootleg cheap copy of tqdm funtion with yield operator
    '''
    steps = len(lst)
    i = 0

    while i <= steps:
        per = i / steps * 100
        bar = i / steps * 66
        i += 1
        percent = f"{int(per):>3}%|["
        fix_bar = f"{'*' * int(bar) + ' ' * (66 - int(bar))}"
        wholenb = f"]| {i-1}/{steps}"
        yield print(percent + fix_bar + wholenb, end='\r')
    # yield print(percent,fix_bar,f"| {i-1}/",f"{steps}", end='\r')
    # yield print(f"{int(per)}%|",fix_bar,f"| {i-1}/",f"{steps}", end='\r')
# yield print(f"{int(per)}%|",f"{'='*int(bar)}",f"|{i-1}/",f"{steps}",end='\r')


# if __name__ == "__main__":
#     main()
# ===============================================================>
# =================================================================>
# █
