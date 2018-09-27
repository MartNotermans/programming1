oldpassword = input('what is your old password?')
newpassword = input('what will be your new password')
if oldpassword != newpassword and len(newpassword) > 5:
    print ('password accepted')
else:
    print ('password not accepted')
