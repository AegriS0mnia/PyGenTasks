indications = input().split()

unique_indications = {int(i) for i in indications}

print(len(indications) - len(unique_indications))


