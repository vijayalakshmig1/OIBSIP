print("BMI Calculator!!!!")
weight_of_candidate = int(input("Enter the weight: "));
height_of_candidate = float(input("Enter the height: "));
BMI = weight_of_candidate/float(height_of_candidate*height_of_candidate);
if BMI < 18.5:
    print('Underweight')
if BMI>=18.5 and BMI<25:
    print('Normal')
if BMI >= 25 and BMI < 30:
   print('Overweight')
if BMI >= 30:
    print('Obesity')
