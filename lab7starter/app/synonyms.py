def get_synonyms_from_files():
    try:
        count = 1 #make a counter of each line
        with open("synonyms.txt") as file:
            lines = file.readlines()
            all_synonyms = {} #creating response variable of dict
            for line in lines: # reading each line
                if not line.strip(): # error if empty line
                    print("Error in line " + str(count) + ":")
                else:
                    data = line.replace('\n', '') # every line has new line. replace it
                    syn_val = data.split(",")
                    syn_data = [p for p in syn_val if p]
                    if len(syn_data) > 1:
                        syn_new = []
                        for k in syn_data: # making list of correct synonyms
                            i = k.strip()
                            if i:
                                syn_new.append(i)
                            else:
                                print("Error in line " + str(count) + ": " + str(data))
                                break
                        for j in syn_new:
                            if j not in all_synonyms.keys(): # checking already key named
                                extact_data = syn_new 
                                all_synonyms[j] = extact_data
                                all_synonyms[j].extend(extact_data)
                                my_data = all_synonyms[j]
                                mylist = list(dict.fromkeys(my_data)) # remove duplicate list value
                                if j in mylist:
                                    mylist.remove(j) # remove key if in list
                                all_synonyms[j] = mylist
                            else:
                                extact_data = syn_new
                                all_synonyms[j].extend(extact_data)
                                my_data = all_synonyms[j]
                                mylist = list(dict.fromkeys(my_data))
                                if j in mylist:
                                    mylist.remove(j)
                                all_synonyms[j] = mylist
                    else:
                        print("Error in line " + str(count) + ": " + str(data))
                count += 1
            return all_synonyms
    except Exception as e:
        print(e)
        all_synonyms = {}
        return all_synonyms
