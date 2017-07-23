try:
    i = [1,2,3,4,5]
    raise IndexError
except(ZeroDivisionError) as e:
    print("Don't divide by zero")
    print(e)
except:
    print('Im here')
finally:
    print("Finished")
