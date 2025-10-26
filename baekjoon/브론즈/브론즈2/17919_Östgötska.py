sentence = input().split()
ae_count = sum(1 for word in sentence if "ae" in word)

if ae_count / len(sentence) >= .4:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
