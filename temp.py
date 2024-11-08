test_string =  "MCMXCIV" # IV
            #   MCMXCIV


def romanToInt(s: str) -> list:
    #reversed_s = s[::-1] 
    values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    res = 0
    result_list = list(map(lambda i:  
                            -values[ s[i]]
                            if i < len(s) - 1 and values[ s[i]] < values[s[i+1]] else values[ s[i]]
                             , range(len(s)) ))
    
    return [result_list, sum(result_list)]


print(romanToInt(test_string))
        

