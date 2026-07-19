a = input()
if(a[0] in "АВЕКМНОРСТУХ"):
    if(a[1] in "123456789"):
        if(a[2] in "123456789"):
            if(a[3] in "123456789"):
                if(a[4] in "АВЕКМНОРСТУХ"):
                    if(a[5] in "АВЕКМНОРСТУХ"):
                        if(a[6] in "_"):
                            if(a[7] in "123456789"):
                                if(a[8] in "123456789"):
                                    print("YES")


                                else:
                                    print("No")
                            else:
                                print("No")
                        else:
                            print("No")
                    else:
                         print("No")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")             
    else:
        print("No")
else:
    print("No")

                       
