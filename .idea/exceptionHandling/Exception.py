# try , except, finally
# In the try block we can take try except and finally block, it is ok.
# Nesting of try, except, finally is also possible.
# To much risky code, we have to take inside nested try block.  
try:                                    #step1
    print("Outer try block")            #step2
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("Outer except block")
finally:
    print("Outer finally block")

# If inner except block has appropriate handler then outer except block will not execute.
# try:
#     stmt-1
#     stmt-2
#     stmt-3
#     try:
#         stmt-4
#         stmt-5
#         stmt-6
#     except xx:
#         stmt-7
#     finally:
#         stmt-8
#     stmt-9
# except:
#     stmt-10
# finally:
#     stmt-11
# stmt-12

# Case-1:(if there is no exception:)
# executable statements: 1,2,3,4,5,6,8,9,11,12
# Case-2:(if an exception is rised at statment 2  and corresponding except block matched then)
# executable statements:1,10,11,12
# Case-3:(if an exception rised at st-2 and corresponding except block not matched)
# it is abnormal termination, but before abnormal termination finally block will execute. executable statements:1,11, this special facility is only for finally block not for other block.
# Case-3:(if an exception rised at st-5 and corresponding inner except matched)
# Executable statements:- 1,2,3,4,7,8,9,11,12(normal termination)
# Case-4:(if an exception is rised at st-5 and corresponding inner except doesn't matched but outer except block matched)
# Executable statemets:-1,2,3,4,only finally(8),10,11,12 (normal termiantion)


