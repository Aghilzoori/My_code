def data_analyze(*adad, operation):
    try:
        if operation == "average":
            return "average", sum(adad) / len(adad)
        elif operation == "max":
            return "max", max(adad)
        elif operation == "sum":
            return "sum", sum(adad)
    except TypeError:
        print("عملیات انجام نشد در اعداد مشکلی هست مقادیر معتبر وارد کنید")
natijeh = data_analyze(2, 5, 9, operation="")
if natijeh == None :
    print("مقادیر معتبر وارد کنید ")
else:
    print(natijeh)