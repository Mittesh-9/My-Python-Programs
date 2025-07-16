def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_dict = {}
        t_dict = {}

        if len(s) == len(t):
            for i in s:
                for j in s:
                    count_s = s.count(i)
                    s_dict.update({i: count_s})

                    count_t = t.count(j)
                    t_dict.update({j: count_t})

                    for key, value in s_dict.items():
                        if key not in t_dict or t_dict[key] == value:
                            print("True")

            print("False")
                        
                        #     return True
                        
                        # return False


                    # print(s_dict)
                    # print(t_dict)


        # if len(s) == len(t):
        #     for i in s



        #     return True

        # return False


if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)



isAnagram("anagram","nagaram")