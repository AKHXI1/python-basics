global_lang='data science'
global_lang1=888

def var_scope_test():
    local_lang='python'
    global_lang=5
    print(local_lang)
    print(global_lang1)
    print(global_lang)


var_scope_test()

print(global_lang)
#print(local_lang)

