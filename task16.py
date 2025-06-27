yosh = int(input("yoshingiz: "))
narh=100000
y_narh=0
if yosh <= 7:
    y_narh=narh*0.5
    print(f"yakuniy narh: {y_narh} (50% chegirma)")
elif yosh <= 18 :
    y_narh= narh * 0.3
    print(f"yakuniy narh: {y_narh} (30% chegirma)")
else:
    print("18 yoshdan kattalarga chegirma yuq")