class multiplefunctions:
    def Subfields():
        print('Sub-fields in AI are:')
        list=['Machine Learning', 'Neural Networks', 'Vision Robotics', 'Speech Processing', 'Natural Language Processing']
        for subfields in list:
            print (subfields)
    def oddeven():
        num=int(input('Enter a number:'))
        if(num%2!=0):
            print(num,'is add number')
        else:
            print(num,'is odd number')
    def Elegible():
        gender=input('Your Gender:')
        num=int(input('Your age:'))
        if(gender=='Male'and num >= 21):
            print('ELEGIBLE')
            ElegibilityForMarriage='ELEGIBLE'
        elif(gender=='Female'and num>=18):
            print('ELEGIBLE')
            ElegibilityForMarriage=('ELEGIBLE')
        else:
            print('NOT ELEGIBLE')
            ElegibilityForMarriage='NOT ELEGIBLE'
        return ElegibilityForMarriage
    def percentage(Subject1,Subject2,Subject3,Subject4,Subject5):
        print('Subject1=',Subject1)
        FindPercent='Subject1=',Subject1
        print('Subject2=',Subject2)
        FindPercent='Subject2=',Subject2
        print('Subject3=',Subject3)
        FindPercent='Subject3=',Subject3
        print('Subject4=',Subject4)
        FindPercent='Subject4=',Subject4
        print('Subject5=',Subject5)
        FindPercent='Subject5=',Subject5
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        Percentage=(Total/500)*100
        print('Total:',Total)
        FindPercent='Total:',Total
        print('Percentage:',Percentage)
        FindPercent='Percentage:',Percentage
        return FindPercent
    def triangle():
        num1=int(input("Height:"))
        num2=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        num3=(num1*num2)/2
        print("Area of Traingle:",num3)
        num4=int(input("Height1:"))
        num5=int(input("Height2:"))
        num6=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        num7=num4+num5+num6
        print("Perimeter of Traingle:",num7)
        return num3,num7
    